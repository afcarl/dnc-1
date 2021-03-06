import numpy as np
import tensorflow as tf
from controller import Controller
from tensorflow.contrib.rnn.python.ops.core_rnn_cell import LSTMStateTuple


"""
A 2-Layer feedforward neural network with 128, 256 nodes respectively
"""

class NNController(Controller):

    def init_controller_params(self):
        h1_dim = 128
        h2_dim = 256
        init = tf.truncated_normal_initializer(stddev=0.1, dtype=tf.float32)

        self.params['W1'] = tf.get_variable("W1", [self.chi_dim, h1_dim], initializer=init)
        self.params['b1'] = tf.get_variable("b1", [h1_dim], initializer=init)
        self.params['W2'] = tf.get_variable("W2", [h1_dim, h2_dim], initializer=init)
        self.params['b2'] = tf.get_variable("b2", [h2_dim], initializer=init)


    def nn_step(self, X, state):
        z1 = tf.matmul(X, self.params['W1']) + self.params['b1']
        h1 = tf.nn.elu(z1)
        z2 = tf.matmul(h1, self.params['W2']) + self.params['b2']
        h2 = tf.nn.elu(z2)
        return h2, state

    def update_state(self, update):
        return tf.group(tf.zeros(1), tf.zeros(1))

    def get_state(self):
        return LSTMStateTuple(tf.zeros(1), tf.zeros(1))
