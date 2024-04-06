# syntax=docker/dockerfile:1

# FROM python:3.9.10-alpine3.14

# WORKDIR /srv
# RUN apk add --no-cache gcc musl-dev linux-headers

# RUN pip install --upgrade pip
# RUN pip install flask
# RUN pip install redis
# RUN pip install debugpy

# COPY . /srv


# ENV FLASK_APP=app
# CMD ["python","app.py"]

# EXPOSE 5000


FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]