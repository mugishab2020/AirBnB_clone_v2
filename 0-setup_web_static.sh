#!/usr/bin/env bash
# updating the system and installing nginx

sudo apt-get update
sudo apt-get install -y nginx

# Create folders required if not already exists
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.hmtl
# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# changing the owner to ubuntu
sudo chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration to serve
config_text="location /hbnb_static/ {
    alias /data/web_static/current/;
}"
sudo sed -i "{config_text}" /etc/nginx/sites-available/default
# nginx restsart
sudo service nginx restart
