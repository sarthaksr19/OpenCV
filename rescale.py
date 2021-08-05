import cv2 as cv

#resizing video

#resclaing using function rescaleFrame

def rescaleFrame(frame, scale=0.75):
    # rescaleFrame works for images, exsited videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # this change resolution works only for live video not for any existed video or image.
    capture.set(3, width)
    capture.set(4, height)

# capture = cv.VideoCapture('video/dance.mp4')  #capture variable is a instance variable of this class i.e, video,'dance.mp4'

# while True:  #while loop grab frame one by one by capture.read method
#     isTrue, frame = capture.read()

#     frame_resize = rescaleFrame(frame, scale=0.2)

#     cv.imshow('dance', frame)  #disaplying eavh frame by writing imshow method
#     cv.imshow('video_resized', frame_resize)

#     if cv.waitKey(5) & 0xff==ord('d'):  #if the key d is pressed break out of loop
#         break

# capture.release()
# cv.destroyAllWindows()

# cv.waitKey(0)

# -----------------------------------------------------------------------------------

# resizing images

image = cv.imread('images/kholi.jpg')
cv.imshow('img1', image)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(image, scale=0.5)
cv.imshow('img', resized_image)

cv.waitKey(0)