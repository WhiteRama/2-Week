import tensorflow as tf
import numpy as np
import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


x = tf.constant(60, name = 'x')
y = tf.Variable(x+7, name = 'y')

model=tf.global_variables_initializer()

sess = tf.Session()

sess.run(model)
print(sess.run(y))

print(x)
print(y)