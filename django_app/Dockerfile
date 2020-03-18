FROM python:3.6.2

LABEL maintainer Asarudheen

ENV PYTHONUNBUFFERED 1

RUN mkdir /src/app

WORKDIR /src/app

COPY . /src/app

RUN pip install -r requirements.txt