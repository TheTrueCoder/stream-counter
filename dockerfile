FROM nginx:alpine
COPY ./api/default.conf /etc/nginx/conf.d/default.conf
COPY ./website /usr/share/nginx/html