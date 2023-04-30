import numpy as np
import cv2
import time











img = np.zeros((500,500, 3))

for i in range (0, 500):
    img2 = np.copy(img)
    img2[300:500, (0+i):(200+i)] = [255,255,255] 
    cv2.imshow('python',img2)
    key  = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()




























