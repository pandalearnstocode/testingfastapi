docker build -t fastapi_tf_gpu .
docker run --gpus all -d -p 80:80 fastapi_tf_gpu