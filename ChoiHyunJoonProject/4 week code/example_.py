import numpy as np
import tensorflow as tf

num_puntos = 1000
conjunto_puntos = []

for i in range(num_puntos):
	x1 = np.random.normal(0.0, 0.55)
	y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
	conjunto_puntos.append([x1, y1])

x_data = [v[0] for v in conjunto_puntos]
y_data = [v[1] for v in conjunto_puntos]

import matplotlib.pyplot as plt
plt.plot(x_data, y_data, 'ro', label='Original data')
plt.legend()
plt.show()

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))

y = W * x_data + b
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)

train = optimizer.minimize(loss)
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(32):
        sess.run(train)
        plt.plot(x_data, y_data, 'ro', label='train_data')
        plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
        plt.xlabel('x')
        plt.xlim(-2, 2)
        plt.ylabel('y')
        plt.ylim(0.1, 0.6)
        plt.legend()
        plt.show()
