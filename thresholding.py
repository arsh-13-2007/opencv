import cv2 as cv
import numpy as np 



img = cv.imread('photo/cat2.jpeg')

# cv.imshow('cat',img)

img_resize = cv.resize(img , (500 , 500))
cv.imshow('Image_resized' ,img_resize)
blank = np.zeros(img_resize.shape[:2] , dtype='uint8')
cv.imshow('blank Image' , blank)

gray = cv.cvtColor(img_resize , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)



# simple thresholding 

thresholding , thresh = cv.threshold(gray , 200 , 255 , cv.THRESH_BINARY)
cv.imshow('simple thresholded' , thresh)


thresholding , thresh_inverse = cv.threshold(gray , 200 , 255 , cv.THRESH_BINARY_INV)
cv.imshow('simple thresholded inverse' , thresh_inverse)

#  adaptive thresholding 

th = cv.adaptiveThreshold(gray, 255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11, 2)
cv.imshow('adaptive thresholding' , th)


# Otsu’s Thresholding (automatic optimal threshold)

# You do not choose a threshold value; OpenCV chooses the best one mathematically.

ret, otsu = cv.threshold(gray, 0, 255,cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imshow('otsu thresholding' , otsu)
cv.waitKey(0)
