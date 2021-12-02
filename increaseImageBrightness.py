import cv2
import numpy as np
import os

def change_brightness(img, alpha, beta):
   return cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype),0, beta)

img_path = "../dataset/NA2 patches/NA2 patches/"
img_out_path = "../dataset/NA2 patches/IncreasedBrightness/"


for i, filename in enumerate(os.listdir(img_path)):
    if filename.endswith(".png") or filename.endswith(".jpg"): 
        img = cv2.imread(img_path+str(i)+".png")
        img = change_brightness(img, 3, 2)
        cv2.imwrite(img_out_path + str(i)+".png", img)
    else:
        continue
