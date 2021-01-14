FROM python:alpine3.7


RUN apk update && apk upgrade

RUN apk add --no-cache --virtual .build-dependencies \
    build-base \
    gcc \
    wget

RUN apk add --no-cache \
    libffi-dev \
    xmlsec-dev \
    musl-dev \
    libressl-dev \
    git

RUN python3.7 -m pip install pipenv

WORKDIR /app

ADD Pipfile Pipfile.lock /app/

RUN pipenv install --system --deploy --ignore-pipfile

ADD . /app

ARG ADMIN_PASSWORD=123456789

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN python manage.py createsuperuser --noinput --email admin@example.com

EXPOSE 8080

CMD ["gunicorn", "--preload", "--bind=0.0.0.0:8080", "--log-level=warning", "auth.wsgi"]
