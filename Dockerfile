FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN pip install --no-cache-dir pandas joblib python-multipart

COPY ./app /app