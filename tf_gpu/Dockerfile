FROM tensorflow/tensorflow:latest-gpu-py3
RUN pip install --no-cache-dir "uvicorn[standard]" gunicorn fastapi pandas joblib python-multipart loguru
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY ./gunicorn_conf.py /gunicorn_conf.py
COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh
COPY ./app /app
WORKDIR /app/
ENV PYTHONPATH=/app
EXPOSE 80
CMD ["/start.sh"]