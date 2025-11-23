import cv2 as cv 
import numpy as np 
#                         drawing shape 
# capture = cv.VideoCapture(0)
blank = np.zeros( (500 , 500 , 3 ) ,dtype ='uint8' )
cv.imshow('blank' , blank)

# blank[:] = (0,255,0)
# cv.imshow('green' , blank)


# blank[200:300 , 300:400] = ( 0 , 255,0)
# cv.imshow('img_second' , blank)


# # draw any shape
# cv.rectangle(blank, (0,0) , (250, 300) , (0,0,255) , thickness=2 )
# cv.imshow('blank' ,  blank)

# cv.rectangle(blank, (0,0) , (250, 300) , (0,0,255) , cv.FILLED )
# cv.imshow('blank' ,  blank)


# cv.line(blank, (0,0) , (250, 300) , (255 , 255,255) , 2 )
# cv.imshow('blank' ,  blank)
# cv.waitKey(0)

#                   putting text on image

img = cv.imread('photo/cat2.jpeg')

cv.putText( img , "this cat", (20,2+0) , cv.FONT_HERSHEY_SIMPLEX  , 1.0  ,(0,0,255) ,thickness=2 )  
cv.imshow('img' , img)

cv.waitKey(0)
cv.destroyAllWindows()



