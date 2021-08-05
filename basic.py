import cv2 as cv

img = cv.imread('images/yuvi.jpg')

cv.imshow('Yuvi', img)

# 1. Converting to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_image', gray)

# 2. Blur
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# to increase the bluryness of image we need to increase kernel size of the image i.el, after the img src.
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# 3. Edge Cascade. detecting all the edges from the images

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny images', canny)

# if we want reduce the edges then we use blur image.
canny_blur = cv.Canny(blur, 125, 175)
cv.imshow('Blury Canny images', canny_blur)

# 4. Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('dilation', dilated)

# Erode. means erosion of soil as in erosion we left some edges as same property applies it erode() also. return the exact canny_blur image with respect to eroded.
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('eroded', eroded)

# 5. Resize
resized = cv.resize(img, (500,500))
cv.imshow('resize', resized)

# 6. Cropping the image
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)





cv.waitKey(0)