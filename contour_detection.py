import cv2 as cv 
import numpy as np 

img = cv.imread("photo/cat3.jpeg")
cv.imshow('img' , img)



img_resize = cv.resize(img , ( 600 , 600))
cv.imshow('resized_image' , img_resize)

blank_img =np.zeros(img_resize.shape[:-2] , dtype='uint8')
cv.imshow('blank' , blank_img)
gray = cv.cvtColor(img_resize ,cv.COLOR_BGR2GRAY)  # converting rgb into grey scale to image 
cv.imshow('grey_img' , gray)

blur = cv.GaussianBlur(gray , ( 3,3) , 0)
cv.imshow('blur' , blur )

canny = cv.Canny(blur, 125 , 175)
cv.imshow('canny' , canny)
#                   contour detection 
contours , hierarchies = cv.findContours(canny , cv.RETR_LIST , cv.CHAIN_APPROX_NONE)
print( len(contours))


contour_img = img_resize.copy()
cv.drawContours(blank_img,contours, -1, (0,0,255) , thickness=1)
cv.imshow('contours' , blank_img)

cv.waitKey(0)
cv.destroyAllWindows()