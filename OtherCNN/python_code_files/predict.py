from keras.models import load_model
from astropy.io.fits import getdata, PrimaryHDU
import keras.backend as K
import pickle
import numpy as np

model = load_model('checkpoint-60.h5')
img = getdata('BadImage.fits')
img = np.array([img.reshape(*(img.shape), 1)])

prediction = model.predict(img)[0]
K.clear_session()
print(prediction.shape)
#hdu = PrimaryHDU(prediction[0])
with open('prediction.h5', 'wb') as f:
	pickle.dump(prediction, f)
