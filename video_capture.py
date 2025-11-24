import cv2 as cv 


haar_cascade = cv.CascadeClassifier('haarcascade_face_default.xml')

capture = cv.VideoCapture(0)
 
while True : 
    success , frame = capture.read()
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_dect = haar_cascade.detectMultiScale(gray ,scaleFactor=1.1 ,minNeighbors= 3)
    
    for x, y, w, h in face_dect:
        cv.rectangle(frame , ( x, y) , ( x+ w, y+ h) , (0 , 255, 255) , 2 )
    cv.imshow('video' , frame)
    if cv.waitKey(1) & 0xff == ord('x'):
        break 

capture.release()
cv.destroyAllWindows()
