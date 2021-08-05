import cv2 as cv

#image reading
# img = cv.imread('images/captain.jpg') #read the images 

# cv.imshow('dhoni', img)  #showing the image with imshow() method this method takes generally two parameter one is name of the file and second one is the variable name where file is stored

# cv.waitKey(0)

#video reading
capture = cv.VideoCapture('video/dance.mp4')  #capture variable is a instance variable of this class i.e, video,'dance.mp4'

while True:  #while loop grab frame one by one by capture.read method
    isTrue, frame = capture.read()
    cv.imshow('dance', frame)  #disaplying eavh frame by writing imshow method

    if cv.waitKey(5) & 0xff==ord('d'):  #if the key d is pressed break out of loop
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)