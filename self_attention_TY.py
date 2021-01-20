# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:50:49 2020

@author: user
"""
import tensorflow.keras.backend as K
EMB_SIZE=128


num_heads= 4
model_dim=EMB_SIZE
key_dim=EMB_SIZE//header
value_dim=EMB_SIZE//header

def linear_projection(q,k,v):
    q = Dense(key_dim, use_bias=False)
    k = Dense(key_dim, use_bias=False)
    v = Dense(key_dim, use_bias=False)

def split_heads(q,k,v):
    def split_last_dimension_then_transpose(tensor, num_heads, dim):
        K.expand_dims(tensor,axis=0)

xx=np.arange(1,65)
xx.reshape(1,8,8)

xx = tf.constant(xx)