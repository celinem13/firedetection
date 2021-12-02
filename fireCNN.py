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
