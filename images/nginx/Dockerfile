FROM nginx:alpine

RUN rm -f /etc/nginx/conf.d/default.conf\
    && echo "daemon off;" >> /etc/nginx/nginx.conf
    
ADD conf /etc/nginx/conf.d/

EXPOSE 80
CMD ["nginx"]