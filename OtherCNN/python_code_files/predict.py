from keras.models import load_model
from astropy.io.fits import getdata, PrimaryHDU
import keras.backend as K
import numpy as np

model = load_model('checkpoint-60.h5')
img = getdata('BadImage.fits')

# Preprocess
img_max = np.max(img)
img /= img_max
img = np.array([img.reshape(*(img.shape), 1)])

prediction = model.predict(img)[0]
prediction = prediction.reshape(prediction.shape[0], prediction.shape[1])
prediction *= img_max

K.clear_session()
print(prediction.shape)
hdu = PrimaryHDU(prediction)
hdu.writeto('prediction.fits')
