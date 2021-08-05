import cv2 as cv
import numpy as np

img = cv.imread('images/kholi.jpg')

cv.imshow('kholi', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#shifting of image
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

# translated = translate(img, -100, -100)  #shifting here 100px left and 100px up
translated = translate(img, 100, 100)  #shifting here 100px right and 100px down
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)

#want to rotate it clockwise just give negative value to the angle.
# rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# rotate the rotated image
rotated_rotated = rotate(rotated, 45)
cv.imshow('rotated_rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #if we are shrinking the image then we go for INTER_AREA, if we enlarging the image then we should go for INTER_LINEAR,INTER_CUBIC cubic is slower but it better as it returns the  high quality.
cv.imshow('resized', resized)

# Flipping. flipcode = 0 for vertically, 1 for horizontally, and -1 for both vaertically and horizontally.
flip = cv.flip(img, -1)
cv.imshow('flip', flip)

# Cropping
cropped = img[50:100, 100:200]
cv.imshow('cropped', cropped)

cv.waitKey(0)