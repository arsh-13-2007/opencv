import cv2 as cv 



#                 method 1 of  resize the video   this same do for image also 


def rescaleFrame(frame , scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width , height)

    return cv.resize(frame , dimensions,interpolation=cv.INTER_AREA )


capture = cv.VideoCapture('video/video1.mp4')

while True:
    isTrue , frame = capture.read()
    frame_resize = rescaleFrame(frame , 0.25)

    cv.imshow('video' , frame)   # original size frame 

    cv.imshow('video_resize' , frame_resize)

    if cv.waitKey(10) & 0xff ==ord('x'):
        break

capture.release()
cv.destroyAllWindows()






#                         method 2  resize the image or video
#                      changeRes method is only use for live video  like = youtube  it is not work for already exsisting video  
   
def changeRes(width , height): 
    capture.set(4 , height)
    capture.set(3, width)

capture = cv.VideoCapture(0)
changeRes(1920 , 1080  )
while True:
    success , frame = capture.read()
    cv.imshow('live_video' , frame )
    if cv.waitKey(1) & 0xff == ord('x'):
        break

capture.release()
cv.destroyAllWindows()
