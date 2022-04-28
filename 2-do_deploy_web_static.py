#!/usr/bin/python3
"""This module supplies `do_pack` and `do_deplpy` functions
"""
from fabric.api import local, put, run, env
from datetime import datetime
from os.path import exists

env.user = 'ubuntu'
env.hosts = ['34.148.228.73', '3.91.201.4']


def do_pack():
    """Generates a .tgz archive
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = "web_static_" + date + ".tgz"
    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(archive))
    if result.succeeded:
        return (archive)
    return (None)


def do_deploy(archive_path):
    """
    Distributes an archive to my web servers
        Args
            archive_path = archive path
    """

    if exists(archive_path) is False:
        return False

    archive = archive_path.split("/")[-1]
    dir_web_static = archive.replace(".tgz", "")
    path_web_static = '/data/web_static/releases/' + dir_web_static
    sym_link = '/data/web_static/current'

    try:
        # Upload the archive to the servers
        put(archive_path, '/tmp')

        # Unpack the archive
        run('mkdir -p ' + path_web_static)
        run('tar -xzf /tmp/{} -C {}'.format(archive, path_web_static))
        run('rm /tmp/{}'.format(archive))

        # Deletes the unpacked main directory
        run('mv -n {0}/web_static/* {0}/'.format(path_web_static))
        run('rm -rf {}/web_static'.format(path_web_static))

        # Configures the symbolic link
        run('rm -rf ' + sym_link)
        run('ln -s {} {}'.format(path_web_static, sym_link))
    except Exception:
        return False
