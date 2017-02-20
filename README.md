### Setup

1. ./build.sh
2. Copy bedrock site to ./bedrock
3. Update .env file (DB_HOST='wordpress_db'
                     DB_NAME='wordpress'
                     DB_PASSWORD='secret'
                     DB_USER='root')
4. docker-compose up -d
5. Browse to http://localhost:8181
6. Create database 'wordpress'
7. (Optional) Import data
8. Browse to http://localhost:8000

### Nginx Update

1. Make modifications in ./images/nginx/conf/inc/
2. ./nginx-update.sh
3. (Optional) fswatch -0 -o ./images/nginx/conf | xargs -0 -n1 ./nginx-update.sh

### Shutdown

1. docker-compose down

### Destrop all - WARNING : This will remove all images

1. docker rmi $(docker images -q)

### Included Software

- PHP 7.0
- Nginx (alpine)
- MySQL 5.7