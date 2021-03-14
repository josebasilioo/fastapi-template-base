FROM python:3.8-slim

WORKDIR /fastApi

COPY ./requirements.txt /fastApi/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /fastApi/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /fastApi/
