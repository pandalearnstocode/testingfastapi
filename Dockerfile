FROM tiangolo/uvicorn-gunicorn:python3.8-slim

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN pip install fastapi pandas joblib python-multipart

COPY ./app /app