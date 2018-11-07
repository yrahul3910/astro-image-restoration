from keras.models import Sequential, Model, load_model
from keras.layers import Conv2D, Activation, Input
from keras.layers.normalization import BatchNormalization
from keras.callbacks import ModelCheckpoint
from tqdm import tqdm
import os
import numpy as np
import pickle

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


# Gather the files
#X_train_files = ['VOC2012/rayleigh_crops/' + x for x in os.listdir('VOC2012/rayleigh_crops')]
#Y_train_files = ['VOC2012/red_crops/' + x for x in os.listdir('VOC2012/red_crops')]
with open('crop_data_x.pickle', 'rb') as f:
    X = pickle.load(f)
    X = X.reshape(*(X.shape), 1)

with open('crop_data_y.pickle', 'rb') as f:
    Y = pickle.load(f)
    Y = Y.reshape(*(Y.shape), 1)

def gen():
    """
    Generates random mini-batches of size 256
    """
    while True:
        r = np.random.randint(0, len(X_train_files) - 255 - 1)
        batch_x_files = X_train_files[r:r+255]
        batch_y_files = Y_train_files[r:r+255]

        batch_x = np.array([plt.imread(x).reshape(35, 35, 1) for x in batch_x_files])
        batch_y = np.array([plt.imread(x).reshape(35, 35, 1) for x in batch_y_files])

        yield (batch_x, batch_y)


# Compile the model
#model = IRCNN()
#model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy', 'mae'])
model = load_model('checkpoint-41.h5')
print('Model loaded.')

# Set up CNN parameters
epochs = 10

#for e in range(epochs):
#    print('Epoch', e, '/', epochs)
#    values = 0    
#    for i in tqdm(range(0, len(X_train_files), 256)):
#        batch_x_files = X_train_files[i:i+255]
#        batch_y_files = Y_train_files[i:i+255]

#        batch_x = np.array([plt.imread(x).reshape(35, 35, 1) for x in batch_x_files])
#        batch_y = np.array([plt.imread(x).reshape(35, 35, 1) for x in batch_y_files])

#        values = model.train_on_batch(batch_x, batch_y)

#    model.save('batch_checkpoints/checkpoint-' + str(e+5) + '.h5')
#    try:
#        print(values)
#    except:
#        pass
checkpointer = ModelCheckpoint('checkpoint-{epoch:02d}.h5')
#model.fit_generator(gen(), epochs=10, steps_per_epoch=len(X_train_files)//256 ,callbacks=[checkpointer])
model.fit(X, Y, batch_size=32, epochs=500, callbacks=[checkpointer], initial_epoch=41)
