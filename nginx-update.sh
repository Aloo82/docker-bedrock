#!/bin/sh
echo "Copying nginx conf"
docker cp ./images/nginx/conf/. dockerbedrock_nginx_1:/etc/nginx/conf.d/
docker exec dockerbedrock_nginx_1 nginx -s reload
