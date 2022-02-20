import numpy as np
from keras.models import Model
from keras.layers import Dense, Input, Lambda
import tensorflow as tf

class Actor(object):
    
    def __init__(self, sess, state_dim, action_dim, action_bound, learning_rate):
        self.sess = sess
