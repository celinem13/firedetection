import rasterio
import numpy as np
import os
import cv2

directory = './'
OUTPUT_DIR = './output'
OUTPUT_IMAGE_NAME = '762.png'

MAX_PIXEL_VALUE = 65535 # Max. pixel value, used to normalize the image

imgcounter = 0

def get_img_762bands(path):
    img = rasterio.open(path).read((7,6,2)).transpose((1, 2, 0))    
    img = np.float32(img)/MAX_PIXEL_VALUE
    
    return img

for filename in os.listdir(directory):
    if filename.endswith(".tif"):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        img = get_img_762bands(directory+filename)
        img = np.array(img * 255, dtype=np.uint8)
        imgfilename = str(str(imgcounter)+".png")
        
        cv2.imwrite(os.path.join(OUTPUT_DIR, imgfilename), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        imgcounter = imgcounter+1
        
        



        



