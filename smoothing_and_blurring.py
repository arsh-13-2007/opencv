import cv2 as cv 
import numpy as np 
#       Blurring (also called smoothing) is a technique used in image processing to reduce noise,
img = cv.imread('photo/cat2.jpeg')

cv.imshow('cat',img)


img_resize = cv.resize(img , (600 , 600))
#           blurring techinque 
# 1. Averaging (Mean Blur)
blur = cv.blur(img_resize , (5,5))
cv.imshow('img_blur' ,blur )



# 2.  gaussian 

gaussian_blur = cv.GaussianBlur( img_resize , (5,5) , 0)
cv.imshow('Gaussian Blur',gaussian_blur)


# 3. median blur 
median_blur = cv.medianBlur( img_resize , 5)
cv.imshow('median Blur',median_blur)


# 4. bilateral filter 
bilateral_blur = cv.bilateralFilter( img_resize ,5 , 75 , 75 )
cv.imshow('bilateral Blur',bilateral_blur)

cv.waitKey(0)
cv.destroyAllWindows()
