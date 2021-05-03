docker build -t fastapi_tf_gpu .
docker run --gpus all -d -p 80:80 fastapi_tf_gpu
docker tag fastapi_tf_gpu cc66856916f64dccb42617f4ad158d83.azurecr.io/fastapi_tf_gpu
docker push cc66856916f64dccb42617f4ad158d83.azurecr.io/fastapi_tf_gpu