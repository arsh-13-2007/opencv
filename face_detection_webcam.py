import cv2 as cv
import numpy as np 


face_cascade = cv.CascadeClassifier('haarcascade_face_default.xml')
capture = cv.VideoCapture(0)
while True:
    success ,frame = capture.read()
    gray = cv.cvtColor(frame ,cv.COLOR_BGR2GRAY)
    face_dect = face_cascade.detectMultiScale(gray , 1.1 , 3 )
    for x , y , w,h in face_dect:
        cv.rectangle(frame , (x , y) , (x+ w , y+ h) , (0, 255, 0) ,thickness= 3 )

    cv.imshow('frame detection' , frame)

    if cv.waitKey(1) & 0xff==ord('x'):
        break

capture.release()
cv.destroyAllWindows()