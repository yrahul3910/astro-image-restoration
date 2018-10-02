import pickle
import numpy as np
import os

files = ['Noisy/' + x for x in os.listdir('Noisy')]
X_all = []
Y_all = []

for file in files:
    with open(file, 'rb') as f:
        data = pickle.load(f)

    X, Y = data['X'], data['Y']
    X_all.append(X)
    Y_all.append(Y)

def get_sample(I,Ip,sz,szp):
    """
    geta  random sample (small image from I of size sz*sz and its corresponding 
    smaller image from Ip of size szp*szp)
    """
    i=np.random.randint(0,I.shape[0]-sz)
    j=np.random.randint(0,I.shape[1]-sz)
    delt=int(np.ceil((sz-szp)*1.0/2))
    if szp==1:
        y=Ip[i+delt,j+delt]
    else:
        y=Ip[i+delt:i+sz-delt,j+delt:j+sz-delt]
    return I[i:i+sz,j:j+sz],y

def get_data_multi(I,Ip,sz,szp,n):
    nbi=len(I)
    xapp=np.zeros((n,1,sz,sz))
    xtest=np.zeros((n,1,szp,szp))
    for i in range(n):
        im=np.random.randint(0,nbi)
        xapp[i,:,:,:],xtest[i,:,:,:]=get_sample(I[im],Ip[im],sz,szp)
    return xapp,xtest 

print('Generating crops')
# Unfortunately, the code generating the pickle files generated X and Y
# in the wrong order (Y is actually X, and vice versa)
Y_crops, X_crops = get_data_multi(Y_all, X_all, 32, 14, 100000)
print('Finished generating crops')
with open('crop_data.pkl', 'wb') as f:
    # This weird saving is to reverse the old mistake
    pickle.dump({'Y_crops': X_crops, 'X_crops': Y_crops}, f)

print('Finished dumping data')
