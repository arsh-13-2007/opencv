import cv2 as cv 
import numpy as np 

# Masking in OpenCV means selecting a specific part of an image using a mask, and hiding or removing the rest.
# Masking = cutting out a portion of an image using another image (the mask).

img = cv.imread('photo/cat2.jpeg')

# cv.imshow('cat',img)

img_resize = cv.resize(img , (500 , 500))
cv.imshow('Image_resized' ,img_resize)
blank = np.zeros(img_resize.shape[:2] , dtype='uint8')
cv.imshow('blank Image' , blank)

mask = cv.circle(blank ,(img_resize.shape[1]//2 , img_resize.shape[0]//2) ,100 , 255 , -1 )
cv.imshow('mask' , mask)
mask = cv.rectangle(blank ,(img_resize.shape[1]//2 , img_resize.shape[0]//2) ,(img_resize.shape[1]//2+200 , img_resize.shape[0]//2+200) , 255 , -1 )
cv.imshow('mask' , mask)

masked = cv.bitwise_and(img_resize , img_resize, mask=mask)
cv.imshow('masked' , masked)








cv.waitKey(0)
cv.destroyAllWindows()