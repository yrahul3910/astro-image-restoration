from astropy.io.fits import getdata, PrimaryHDU
from keras.models import load_model

model = load_model('checkpoint-250.h5')
data = getdata('M13V20080421.fits')
data = data.reshape(*(data.shape), 1, 1)

prediction = model.predict(data)
prediction = prediction.reshape(prediction.shape[0], prediction.shape[1])
hdu = PrimaryHDU(prediction)
hdu.writeto('M13V20080421_prediction.fits')
