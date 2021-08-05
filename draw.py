import cv2 as cv
import numpy as np

#blank image
blank = np.zeros((500,500,3), dtype='uint8')
# uint8 is basically a image with datatype of uint8
cv.imshow('blank', blank)

# optional. if we want to take some image that is already exsited in our system.
# img = cv.imread('images/dhoni.jpg')
# cv.imshow('image', img)

# 1. paint the image a certain colour
# blank[:] = 0,0,255
# cv.imshow('Green', blank)

# 2. painting a particular pixel
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('red', blank)

# 3. draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
# cv.imshow('rectangle', blank)

# filling the rectangle 
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
# another way to write instead of giving a fixed value and thickness 
# cv.rectangle(blank, (0,0), (blank.shape[1]//2 , blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('rectangle', blank)

# 4. Draw a circle
# cv.circle(blank, (250,250), 80, (0,0,255), thickness=2)
# # cv.circle(blank, (250,250), 80, (0,0,255), thickness=cv.FILLED) #or -1
# cv.imshow('circle', blank)

# 5. Draw a line
# cv.line(blank, (0,0), (250,250), (0,0,255), thickness=2)
#  another way to write above line function with different type of argument but work as same as above line expcept color
# cv.line(blank, (0,0), (blank.shape[1], blank.shape[0]//2), (255,255,255), thickness=2)
# cv.imshow('line', blank)

# 6. Write text on image
cv.putText(blank, 'Hello, My Name is Sarthak!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)