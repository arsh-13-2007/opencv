import cv2 as cv
import numpy as np 

# direct live drawing on photo 
flag = False
ix= -1 
iy = -1 

def draw(event, x, y, flags, params):
    global flag , ix, iy
    if event == 1:      # left click
       flag = True 
       ix = x 
       iy = y 
    elif event ==  0:
        
        if flag == True:
            
            cv.rectangle(resize_img ,pt1=(ix ,iy) ,pt2= ( x, y) ,color= (0, 255, 255) , thickness=1)
    elif event == 4:

        flag = False
        cv.rectangle(resize_img ,pt1=(ix ,iy) ,pt2= ( x, y) ,color= (0, 255, 255) , thickness=1)

# use SAME window name everywhere
cv.namedWindow(winname="window")
cv.setMouseCallback("window", draw)

img = cv.imread('photo/cat2.jpeg')
resize_img = cv.resize(img, (500, 500))
while True:
    cv.imshow('window', resize_img)

    if cv.waitKey(1) & 0xFF == ord('x'):
        break

cv.destroyAllWindows()
