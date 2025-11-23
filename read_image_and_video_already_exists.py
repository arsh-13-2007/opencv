import cv2 as cv
import time

 # reading images 
# img = cv.imread('photo/cat2.jpeg')

# cv.imshow('cat',img)
# cv.waitKey(0)
# # reading video 
capture  = cv.VideoCapture(0)   #  0  is refer to camera 
#  # how to read already video 

capture = cv.VideoCapture('video/video2.mp4')

while True:
    isTrue , frame = capture.read()
    cv.imshow('video' , frame)
    if cv.waitKey(10) & 0xff== ord('x'):
        break
capture.release()
cv.destroyAllWindows()