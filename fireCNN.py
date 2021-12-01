import tensorflow as tf
import cv2

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

# Normalize pixel values to be between 0 and 1
#train_images, test_images = train_images / 255.0, test_images / 255.0
#print(train_images[0])

#plt.imshow(train_images[0])
#plt.show()

print(train_labels.shape)

img_path = "../dataset/NA2 patches/NA2 patches/"

img = cv2.imread(img_path +"0.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
h, s, v = cv2.split(hsv)

lim = 255 - 30
v[v > lim] = 255
v[v <= lim] += 30

final_hsv = cv2.merge((h, s, v))

cv2.imshow("img",hsv)
cv2.imshow("img2",final_hsv)
cv2.waitKey(0)

#train_images = 0
#train_labels = 0

#test_images = 0
#test_labels = 0

#model = models.Sequential()
#model.add(layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu', input_shape=(256,256,1)))
#model.add(layers.MaxPooling2D(2,2))
#model.add(layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
#model.add(layers.MaxPooling2D(2,2))
#model.add(layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
#model.add(layers.MaxPooling2D(2,2))
#model.add(layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
