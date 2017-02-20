### Setup

1. ./build.sh
2. docker-compose up
3. Browse to http://localhost:8181
4. Create database 'wordpress'
5. (Optional) Import data
6. Copy bedrock site to ./bedrock
7. Update .env file (DB_HOST='wordpress_db'
                     DB_NAME='wordpress'
                     DB_PASSWORD='secret'
                     DB_USER='root')
8. Browse to http://localhost:8000

### Nginx Update

1. Make modifications in ./images/nginx/conf/inc/
2. ./nginx-update.sh dockerbedrock_nginx_1

### Included Software

- PHP 7.0
- Nginx (alpine)
- MySQL 5.7