#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

## Install Nginx
sudo apt update
sudo apt install -y nginx

## Creates the folders and index.html
sudo mkdir -p /data/web_static/{releases,shared}
sudo mkdir -p /data/web_static/releases/test
sudo chown -R ubuntu:ubuntu /data
echo "Test my configuration file" > /data/web_static/releases/test/index.html

## Creates symbolic link
sym_link="/data/web_static/current"
sudo ln -sf /data/web_static/releases/test/ "$sym_link"

## Modify the Ngnix configuration file to deploy a web_static
location_block="\n\tlocation /hbnb_static/ {\n\t\talias $sym_link;\n\t}\n"
sudo sed -i "/server_name _;/ a \\$location_block" /etc/nginx/sites-available/default

sudo service nginx restart
