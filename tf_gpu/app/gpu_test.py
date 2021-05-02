import tensorflow as tf
from tensorflow.python.client import device_lib
from loguru import logger
import time

def cpu():
    with tf.device("/cpu:0"):
        random_image_cpu = tf.random.normal((100, 100, 100, 3))
        net_cpu = tf.keras.layers.Conv2D(32, 7)(random_image_cpu)
        return tf.math.reduce_sum(net_cpu)
def gpu():
    with tf.device("/device:GPU:0"):
        random_image_gpu = tf.random.normal((100, 100, 100, 3))
        net_gpu = tf.keras.layers.Conv2D(32, 7)(random_image_gpu)
        return tf.math.reduce_sum(net_gpu)

def get_available_devices():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos]

def gpu_check():
    logger.info("******************************************************")
    logger.info("******************************************************")
    logger.info("******************************************************")
    logger.info("******************************************************")
    logger.info("******************************************************")
    logger.info("******************************************************")
    logger.info("\n\n\n")
    logger.info(tf.version)
    logger.info("\n\n\n")
    logger.info(tf.config.list_physical_devices('GPU'))
    logger.info("\n\n\n")
    logger.info(tf.test.is_gpu_available())
    logger.info("\n\n\n")
    logger.info(tf.test.is_built_with_cuda())
    logger.info("\n\n\n")
    logger.info(get_available_devices()) 
    logger.info("\n\n\n")
    device_name = tf.test.gpu_device_name()
    if device_name != "/device:GPU:0":
        logger.info("\n\n\n")
        logger.info(
            """This error most likely means that this notebook is not configured to use a GPU.  Change this in Notebook Settings via the command palette (cmd/ctrl-shift-P) or the Edit menu."""
        )
        logger.info("\n\n\n")
        raise SystemError("GPU device not found")
    logger.info("\n\n\n")
    logger.info(
        "Time (s) to convolve 32x7x7x3 filter over random 100x100x100x3 images (batch x height x width x channel). Sum of ten runs."
    )
    logger.info("\n\n\n")
    logger.info("CPU (s):")
    start_time = time.time()
    for _ in range(100):
        cpu()
    logger.info("\n\n\n")
    logger.info("--- %s seconds ---" % (time.time() - start_time))
    logger.info("\n\n\n")
    logger.info("GPU (s):")
    logger.info("\n\n\n")
    start_time = time.time()
    for _ in range(100):
        gpu()
    logger.info("--- %s seconds ---" % (time.time() - start_time))
    logger.info("\n\n\n")
    logger.info("******************************************************")
    logger.info("******************************************************")
    logger.info("******************************************************")
    logger.info("******************************************************")
    logger.info("******************************************************")
    logger.info("******************************************************")

