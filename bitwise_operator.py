import cv2 as cv
import numpy as np 

#            bitwise operator 

blank = np.zeros((400 , 400) , dtype = 'uint8')

rectangle = cv.rectangle(blank.copy()  , (30,30), (370, 370) , (255, 255, 255), -1)
circle = cv.circle(blank.copy()  , (200,200), 200 , (255, 255,255)  , -1)

cv.imshow('circle' , circle)
cv.imshow('rectangle' , rectangle)



# bitwise AND     ---->  give  intersecting region 

bitwise_and = cv.bitwise_and(circle , rectangle)
cv.imshow('bitwise_and' , bitwise_and)

# bitwise or   -----> give non intersecting region  adn also intersecting region 
bitwise_or = cv.bitwise_or(circle , rectangle)
cv.imshow('bitwise_or' , bitwise_or)

# bitwise not    -----> reverse the original image 

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise_not' , bitwise_not)

# bitwise xor      ---> give non intersecting region 
bitwise_xor = cv.bitwise_xor(circle , rectangle)
cv.imshow('bitwise_xor' , bitwise_xor)

cv.waitKey(0)
cv.destroyAllWindows()