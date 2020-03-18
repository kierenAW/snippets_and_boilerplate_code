print("Checking which device Tensorflow is using....")
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
import tensorflow as tf
print(tf.test.gpu_device_name())