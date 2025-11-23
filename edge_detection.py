import cv2 as cv 
import numpy as np 


img = cv.imread('photo/cat2.jpeg')

# cv.imshow('cat',img)

img_resize = cv.resize(img , (600 , 600))
cv.imshow('Image_resized' ,img_resize)

gray = cv.cvtColor(img_resize , cv.COLOR_BGR2GRAY)
cv.imshow('gray_image' , gray)

# canny edge detection 
# laplacian  edge detect 
lap = cv.Laplacian(gray , cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian' ,lap )


# sobel  edge detector 
sobelx = cv.Sobel( gray , cv.CV_64F , 1, 0)
sobely = cv.Sobel(gray , cv.CV_64F , 0, 1 )
combined_sobel =cv.bitwise_or(sobelx , sobely)

cv.imshow('soble  Y' , sobely)
cv.imshow('soble  X' , sobelx)
cv.imshow('combined sobel' , combined_sobel)


# canny detector

canny = cv.Canny(gray , 125 , 175)
cv.imshow('canny' , canny) 

cv.waitKey(0)