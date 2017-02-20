#!/bin/bash
docker cp ./images/nginx/conf/. $1:/etc/nginx/conf.d/
docker exec $1 nginx -s reload