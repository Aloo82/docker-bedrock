#!/bin/bash
# Create nginx image
docker build -t aloo/bedrock-nginx ./images/nginx/
# Create php image
docker build -t aloo/bedrock-php ./images/php/