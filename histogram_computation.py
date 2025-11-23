import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread('photo/cat2.jpeg')

img_size = cv.resize(img , (600, 600))
cv.imshow('img_size' , img_size)
#                         histogram on gray image 
# gray = cv.cvtColor(img_size , cv.COLOR_BGR2GRAY)
# cv.imshow('gray_image' , gray )

blank = np.zeros(img_size.shape[:2],dtype='uint8')
cv.imshow('blank_image' , blank)

mask = cv.circle(blank, (img_size.shape[1]//2 , img_size.shape[0]//2) ,100 , 255 , -1 )
masking = cv.bitwise_and(img_size , img_size , mask = mask)
cv.imshow('masking' , masking)
# #  bgr into gray scale


# # grayscale histogram 

# gray_hist  = cv.calcHist([gray] ,[0] ,masking,[256] ,[0, 256])
# plt.title('histgram for gray scale')
# plt.xlabel('Bins')
# plt.ylabel('# pixels')
# plt.plot(gray_hist)
# plt.show()


#                           histogram on color image 

plt.title(' colored histgram')
plt.xlabel('Bins')
plt.ylabel('# pixels')


color = ('b' , 'g' , 'r')
for i, col in enumerate(color):
    hist = cv.calcHist([img_size] , [i] , mask, [256] , [0, 256])
    plt.plot( hist , color = col)
    plt.xlim([0, 256])
   
plt.show()
cv.waitKey(0)
