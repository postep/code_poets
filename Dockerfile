FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL ./static
ENV STATIC_PATH /var/www/tmp
COPY ./requirements.txt /var/www/requirements.txt
COPY ./ /app
RUN chmod -R 777 /app
RUN mkdir -p /var/www/tmp
RUN chmod -R 777 /var/www/tmp
WORKDIR /var/www/tmp



RUN pip install -r /var/www/requirements.txt