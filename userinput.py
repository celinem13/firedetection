import os
import cv2
import numpy as np

img_path = './'
output_dir = './result/result.npy'
result = []
for i, file in enumerate(os.listdir(img_path)):
    if file.endswith('.png'):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        filename = str(i) + ".png"
        img = cv2.imread(os.path.join(img_path, filename))
        resratio = 3
        imS = cv2.resize(img, (256 * resratio, 256 * resratio))  # Resize image
        cv2.namedWindow(filename)
        cv2.moveWindow(filename,600,150)  # Screen position
        cv2.imshow(filename, imS)
        esc = False
        while True:
            key = cv2.waitKeyEx(0)
            if key == 2424832:
                print('left')
                result.append(0)
                break
            elif key == 2555904:
                print('right')
                result.append(1)
                break
            elif key == 27:
                print('esc')
                esc = True
                break
            else:
                continue
        cv2.destroyWindow(filename)
        if esc:
            break

np.save(output_dir, np.array(result))
print(np.load(output_dir))
