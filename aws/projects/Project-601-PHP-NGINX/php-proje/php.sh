#!/bin/bash

apt update -y 
apt upgrade -y
apt install git -y
apt install php7.4 php7.4-fpm -y 
apt install nginx -y
TOKEN="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"
git clone https://$TOKEN@github.com/muhammetguzel/php-proje
rm -rf /var/www/html/index.nginx-debian.html
cd /home/ubuntu/php-proje
cp -r * /var/www/html 
