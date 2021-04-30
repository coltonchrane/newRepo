#computer vision library
import cv2

#name the window
cv2.namedWindow("Assignment5.7")
#set variable to video capture
vc = cv2.VideoCapture(0)
#rval is tracker for window if opned
if vc.isOpened(): #try to get first frame
    rval, frame = vc.read()
else:
    rval = False
while rval:
    #any operation on the frame come to imshow
    #while open push each frame into the window
    cv2.imshow("Assignment5.7", frame)
    rvale, frame = vc.read()
    #read keys
    #waht keyt is pressed
    key = cv2.waitKey(20)

    #look for esc key (Ascii value is 27)
    if key ==27: #exit on esc
        break

    #aftert breaking loop
cv2.destroyWindow("Assignment5.7")
