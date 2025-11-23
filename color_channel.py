import cv2 as cv 
import numpy as np 


img = cv.imread('photo/cat2.jpeg')

cv.imshow('cat',img)


img_resize = cv.resize(img , (600 , 600))
cv.imshow('img_resize' , img_resize)
#                 split 
b, g,r = cv.split(img_resize)

cv.imshow('blue' ,b)
cv.imshow('green' ,g)
cv.imshow('red' ,r)

#        after merge it return original image 
img_merge = cv.merge([b,g,r])
cv.imshow('merge_image' , img_merge)
cv.waitKey(0)
cv.destroyAllWindows()