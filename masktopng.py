import numpy as np
import cv2
import os

directory='./'
OUTPUT_DIR = './output'
OUTPUT_NAME = 'mask.png'
mask_counter=0;
for filename in os.listdir(directory):
    if filename.endswith(".tif"):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        mask_path = directory+filename
        mask = cv2.imread(mask_path)
        copy = cv2.imread(mask_path)
        height, width, depth = mask.shape
        for i in range(0, height):
            for j in range(0, width):
                if (mask[i,j,0] > 0):
                    copy[i,j] = 255
        maskfilename = str(str(mask_counter)+".png")
        print(maskfilename)
        cv2.imwrite(os.path.join(OUTPUT_DIR, maskfilename), copy)
        mask_counter+=1
