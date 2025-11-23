import cv2 as cv
import numpy as np

img = cv.imread('photo\cat3.jpeg')
cv.imshow('img', img)
img_resize = cv.resize(img  , ( 600 , 600))
cv.imshow('img_resize' , img_resize)
# image transforamtion    
#             1).   move image in x or y axis 
def translate( img , x , y ):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img , transMat , dimensions)


# -x = left
# -y = up 
# x = right
# y = down

translated = translate( img_resize ,100 , 100) # right down 
translated = translate( img_resize ,-100 , 100) # left down 
translated = translate( img_resize ,100 , -100) # right up 
translated = translate( img_resize ,-100 , -100)# left up 

cv.imshow('translated' , translated)


#                      2). rotate the image 

def rotate(img , angle , rotpoint=None):
    (height,width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = ( width//2 ,height//2)
    rotMat = cv.getRotationMatrix2D(rotpoint , angle , 1.0)
    dimension = (width,height)

    return cv.warpAffine(img,rotMat,dimension)


rotated = rotate( img_resize , 45 )
rotated = rotate( img_resize , -45 )
cv.imshow('rotated' , rotated)


# flipping 

flip = cv.flip(img_resize , 0 )
cv.imshow('flip' , flip)

 
cv.waitKey(0)
cv.destroyAllWindows()
