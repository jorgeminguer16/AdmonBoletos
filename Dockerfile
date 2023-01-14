FROM python:3.7.9-alpine3.13
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

COPY . /flask_app
WORKDIR /flask_app

RUN chmod -R o+rX .

RUN apk add --update --no-cache g++ gcc libxml2-dev libxslt-dev python3-dev libffi-dev openssl-dev make
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev 

RUN apk del build-deps
RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000
CMD ["python3","wsgi.py"]