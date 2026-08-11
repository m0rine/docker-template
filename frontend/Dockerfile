FROM nginx:latest AS base
LABEL Author="Daniel Morine"
EXPOSE 80/tcp

FROM base AS prod
COPY ./static /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf 


