import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('./IMAGES/sample1.jpg', 1)

# Plotting images using matplotlib 
new_img = img[::, ::, ::-1]

cv2.imshow('image',img)
plt.imshow(new_img)
plt.xticks([]), plt.yticks([])
plt.show()
