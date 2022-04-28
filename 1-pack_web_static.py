#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder
   of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


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
