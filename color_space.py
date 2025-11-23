import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 
img = cv.imread('photo/cat2.jpeg')

cv.imshow('cat',img)

# bgr  to rgb # computer read our image in form of rgb 
# plt.imshow(img)
# plt.show()

img_resize = cv.resize(img , (600 , 600))
# bgr to grayscale 
gray = cv.cvtColor(img_resize , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)


# bgr to hSV

hsv = cv.cvtColor(img_resize , cv.COLOR_BGR2HSV)
cv.imshow('hsv' , hsv)
 # bgr to LAB
lab = cv.cvtColor(img_resize , cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# bgr to rgb 
rgb = cv.cvtColor(img_resize, cv.COLOR_BGR2RGB)
cv.imshow('rgb' , rgb)

cv.waitKey(0)