FROM python:3.6.2

LABEL maintainer Asarudheen

ENV PYTHONUNBUFFERED 1

RUN mkdir /django_app

WORKDIR /django_app

COPY . /django_app

RUN pip install -r requirements.txt
