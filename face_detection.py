import cv2 as cv 
import numpy as np 

img = cv.imread('photo/face1.jpg')
# cv.imshow('face_image' , img)

img_resize = cv.resize(img , ( 750 , 500))
cv.imshow('resized image' , img_resize)

gray = cv.cvtColor(img_resize , cv.COLOR_BGR2GRAY)
# cv.imshow('gray image' , gray)

# blur = cv.GaussianBlur(gray , (5, 5) , 0 )

# median_blur = cv.medianBlur(gray , 7) 

cropped = gray[:  , 10:   ]

# cv.imshow('cropped' , cropped)-

haar_cascade = cv.CascadeClassifier('haarcascade_face_default.xml')

# Detect faces
face_rect = haar_cascade.detectMultiScale(cropped, scaleFactor=1.1, minNeighbors=2)

for (x, y, w, h) in face_rect:
    cv.rectangle(img_resize, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow("Faces Detected", img_resize)
cv.waitKey(0)
cv.destroyAllWindows()