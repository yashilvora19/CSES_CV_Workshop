from cv2 import cv2 
import numpy as np

home = cv2.imread('IMAGES/home.jpg')
logo = cv2.imread('IMAGES/smarties.png')

h,w,n = logo.shape

cut = home[0:h,0:w]

# x = cv2.add(logo,cut)                     THESE 2 DONT WORK- LEAVE THEM COMMENTED OUT
# x = cv2.addWeighted(logo,0.8,cut,0.2,0)

logo_gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

ret,mask = cv2.threshold(logo_gray,200,255,cv2.THRESH_BINARY_INV)   

mask_inv = cv2.bitwise_not(mask)

logo1 = cv2.bitwise_and(logo,logo,mask = mask)        


cut = cv2.bitwise_and(cut,cut,mask = mask_inv)


out = cv2.add(logo1,cut)         

home[0:h,0:w] = out


cv2.imshow("home",home)
cv2.imshow("logo_gray",logo_gray)
cv2.imshow("INVERTED MASK",mask_inv)

cv2.imshow("mask",mask)
cv2.imshow("logo1",logo1)
cv2.imshow("cut",cut)

# cv2.imshow("out",out)




# cv2.imshow("cut",cut)


cv2.waitKey(0)
cv2.destroyAllWindows()
