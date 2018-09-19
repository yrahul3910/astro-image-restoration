from keras.models import Sequential, Model
from keras.layers import Conv2D, Activation, Input
from keras.layers.normalization import BatchNormalization
from matplotlib import pyplot as plt
from tqdm import tqdm
import os
import numpy as np

def IRCNN(input_shape=(None, None, 1)):
    X_input = Input(input_shape)

    X = Conv2D(filters=1, kernel_size=3, dilation_rate=1, padding='same')(X_input)
    X = Activation('relu')(X)

    X = Conv2D(filters=64, kernel_size=3, dilation_rate=2, padding='same')(X)
    X = BatchNormalization()(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=64, kernel_size=3, dilation_rate=3, padding='same')(X)
    X = BatchNormalization()(X)
    X = Activation('relu')(X)
    
    X = Conv2D(filters=64, kernel_size=3, dilation_rate=4, padding='same')(X)
    X = BatchNormalization()(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=64, kernel_size=3, dilation_rate=3, padding='same')(X)
    X = BatchNormalization()(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=64, kernel_size=3, dilation_rate=2, padding='same')(X)
    X = BatchNormalization()(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=1, kernel_size=3, dilation_rate=1, padding='same')(X)

    model = Model(inputs=X_input, outputs=X, name='IRCNN')
    return model


# Compile the model
model = IRCNN()
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy', 'mae'])

# Gather the files
X_train_files = ['VOC2012/train_rayleigh/' + x for x in os.listdir('VOC2012/train_rayleigh')]
Y_train_files = ['VOC2012/train_red_channel/' + x for x in os.listdir('VOC2012/train_red_channel')]

X_test_files = ['VOC2012/test_rayleigh/' + x for x in os.listdir('VOC2012/test_rayleigh')]
Y_test_files = ['VOC2012/test_red_channel/' + x for x in os.listdir('VOC2012/test_red_channel')]

# Set up CNN parameters
epochs = 10
training_data = list(zip(X_train_files, Y_train_files))

# Run the model, saving along the way
for e in range(epochs):
    print('epoch', e)
    for i in tqdm(range(len(training_data))):
        batch = training_data[i]
        X_train = batch[0]
        Y_train = batch[1]

        X = []
        Y = []

        img = plt.imread(X_train)
        img = img.reshape(*(img.shape), 1)
        X.append(img)

        img = plt.imread(Y_train)
        img = img.reshape(*(img.shape), 1)
        Y.append(img)

        model.train_on_batch(np.array(X), np.array(Y))
        
        if i % 500 == 0:
            model.save('checkpoint-' + str(e) + '-' + str(i) + '.model')
            print('Saved checkpoint')
