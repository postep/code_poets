FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL ./static
ENV STATIC_PATH /app
COPY ./requirements.txt /var/www/requirements.txt
COPY ./ /app
RUN chmod -R 777 /app
RUN chmod -R 777 /tmp
WORKDIR /tmp



RUN pip install -r /var/www/requirements.txt
WORKDIR /var/tmp/