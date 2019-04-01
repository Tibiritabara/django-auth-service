FROM python:3.7

WORKDIR /app

COPY . /app

ENV DEBUG True
RUN apt-get -y update
RUN apt-get install -y python python-pip python-dev
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
EXPOSE 80