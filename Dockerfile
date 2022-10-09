FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /google
COPY . /google//
RUN pip install -r requirements.txt
CMD gunicorn google_db.wsgi:application --bind 0.0.0.0:$PORT
