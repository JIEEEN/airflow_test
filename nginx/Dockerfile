FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./www/index.html /usr/share/nginx/html/index.html