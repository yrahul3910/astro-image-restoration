from keras.models import Sequential, Model
from keras.layers import Conv2D, Activation, Input
from keras.callbacks import ModelCheckpoint, EarlyStopping
import os
import numpy as np
import pickle

def cnn_model(input_shape=(None, None, 1)):
    X_input = Input(input_shape)

    X = Conv2D(filters=64, kernel_size=10, padding='valid')(X_input)
    X = Activation('relu')(X)

    X = Conv2D(filters=16, kernel_size=6, padding='valid')(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=1, kernel_size=5, padding='valid')(X)
    X = Activation('relu')(X)

    model = Model(inputs=X_input, outputs=X)
    return model

print('Loading data')
with open('crop_data.pkl', 'rb') as f:
    data = pickle.load(f)
    X, Y = np.array(data['X_crops']), np.array(data['Y_crops'])
    X = np.moveaxis(X, 1, 3)
    Y = np.moveaxis(Y, 1, 3)
    print(X.shape, Y.shape)

print('Creating model')
model = cnn_model()
checkpointer = ModelCheckpoint('checkpoint-{epoch:02d}.h5')
#stopper = EarlyStopping(monitor='val_loss', patience=1, verbose=1)
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy', 'mae'])
model.fit(X, Y, batch_size=50, epochs=30, callbacks=[checkpointer], validation_split=0.1)

print('Done!')
