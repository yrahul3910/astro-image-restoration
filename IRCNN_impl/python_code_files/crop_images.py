from random import randint
from PIL import Image
from scipy import stats as st
import os
import numpy as np
from tqdm import tqdm

def get_random_crop(img, dx, dy):
    x_max, y_max = img.shape
    x = randint(0, x_max - dx - 1)
    y = randint(0, y_max - dy - 1)
    
    return img[x:x+dx, y:y+dy]


def get_n_crops(img, n, dx, dy):
    crops = []
    for i in range(n):
        crops.append(get_random_crop(img, dx, dy))
    
    return crops


def add_rayleigh_noise(img):
    noise = st.rayleigh.rvs(loc=-50.90199985022714, scale=71.70478968403172, size=img.shape)
    return img + noise


files = os.listdir('VOC2012/train_red_channel')

# Generate the crops and their noisy counterparts
for i in tqdm(range(len(files))):
    file = files[i]
    data = np.array(Image.open('VOC2012/train_red_channel/' + file))
    crops = get_n_crops(data, 25, 35, 35)
    noisy = [add_rayleigh_noise(x) for x in crops]
    
    for j in range(25):
        red_im = Image.fromarray(crops[j])
        ray_im = Image.fromarray(noisy[j])
        red_im = red_im.convert('L')
        ray_im = ray_im.convert('L')
        
        red_im.save('VOC2012/red_crops/' + file.split('.')[0] + '-' + str(j) + '.png')
        ray_im.save('VOC2012/rayleigh_crops/' + file.split('.')[0] + '-' + str(j) + '.png')

