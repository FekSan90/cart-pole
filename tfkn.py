#from keras.models import Sequential
#from keras.layers.core import Dense, Dropout, Activation
#from keras.optimizers import SGD
import tensorflow as tf
from numpy import genfromtxt
import numpy as np
from tensorflow import keras
import h5py
# Define the input and the expected output

X = genfromtxt("inlog.csv", delimiter=',')
y = genfromtxt("outlog.csv", delimiter=',')
y = np.reshape(y,(-1,1))

#X = np.array([[0,0],[0,1],[1,0],[1,1]])
#y = np.array([[0],[1],[1],[0]])

# The Sequential model is a linear stack of layers.
model = tf.keras.models.Sequential()
# The model needs to know what input shape it should expect. For this reason, the first layer in a  Sequential model (and only the first, because following layers can do automatic shape inference) needs to receive information about its input shape.
# Some 2D layers, such as Dense, support the specification of their input shape via the argument input_dim 
model.add(tf.keras.layers.Dense(4,input_dim = 4, kernel_initializer='normal', activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(5, kernel_initializer='normal', activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(1))

# Before training a model, you need to configure the learning process, which is done via the compile method
# It receives three arguments:
# - An optimizer (e.g. SGD - Stochastic gradient descent optimizer)
# - A loss function
# For a binary classification problem: binary_crossentropy
# For a mean squared error regression problem: mse
# For a multi-class classification problem: categorical_crossentropy
# - A list of metrics
# For any classification problem you will want to set this to metrics=['accuracy'].
model.compile(loss='mean_squared_error', optimizer='adam')
# Keras models are trained on Numpy arrays of input data and labels. For training a model, you will typically use the fit function.
model.fit(X, y, batch_size=10, epochs=10000)
print(np.round(model.predict_proba(X),2))

# save model to file
model.save("YZ2ZBA.hdf5",True,True)
