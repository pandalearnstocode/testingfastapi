FROM tensorflow/tensorflow:latest-gpu-py3
RUN pip install --no-cache-dir "uvicorn[standard]" gunicorn fastapi pandas joblib python-multipart loguru
RUN pip install --no-cache-dir pyarrow
COPY ./app /app
WORKDIR /app/
ENV PYTHONPATH=/app
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY ./gunicorn_conf.py /gunicorn_conf.py
COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh
EXPOSE 80
CMD ["/start.sh"]