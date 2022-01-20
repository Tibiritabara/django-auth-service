FROM python:3.9-slim

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y \
    build-essential \
    gcc \
    wget \
    libffi-dev \
    xmlsec1 \
    musl \
    libssl-dev

RUN python -m pip install pipenv

WORKDIR /app

ADD Pipfile Pipfile.lock /app/

RUN pipenv install --system --deploy --ignore-pipfile

COPY src/. /app

# ARG ADMIN_PASSWORD=123456789

# RUN python manage.py migrate

# RUN python manage.py collectstatic --noinput

# RUN python manage.py createsuperuser --noinput --email admin@example.com

CMD ["gunicorn", "--preload", "--bind=0.0.0.0:8080", "--log-level=warning", "auth.wsgi"]
