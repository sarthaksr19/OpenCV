# IMPORTING MODULE
import cv2 as cv
import numpy as np

# READING IMAGE
img = cv.imread("images\kholi.jpg")

# GETTING EDGES
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 3)
edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)

# CARTOONIZATION
color = cv.bilateralFilter(img, 9, 250, 250)
cartoon = cv.bitwise_and(color, color, mask=edges)

# SHOWING OUTPUT
cv.imshow('img', img)
cv.imshow('edges', edges)
cv.imshow('cartoon', cartoon)

cv.waitKey(0)