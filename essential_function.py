import cv2 as cv
# comverting image into grayscale 

img = cv.imread('photo/cat2.jpeg')
img1 = cv.imread('photo/cat3.jpeg')
cv.imshow('img' ,img )
cv.imshow('img1' ,img1 )

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

# how to blur the image 
blur_img = cv.GaussianBlur(img1,(3,3) , cv.BORDER_DEFAULT)
cv.imshow('blur' , blur_img)



# Egde cascade 
canny = cv.Canny( img , 125 , 175 )
cv.imshow('canny edge' , canny)


# dilated egde 

dilated = cv.dilate(canny , (7,7) ,iterations =3 )
cv.imshow('dilated' , dilated)

# resize 
resize = cv.resize(img , (500 , 500))
cv.imshow('resize' ,resize)


# cropping 
cropped = resize[50:200 , 200 : 400]
cv.imshow('cropped' , cropped)
cv.waitKey(0)
