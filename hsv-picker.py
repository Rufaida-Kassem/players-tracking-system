import numpy as np
np.set_printoptions(threshold=np.nan)
import numpy.linalg as la
import cv2 as cv
# import cv2 as cv.cv as cv
import math
import matplotlib.pyplot as plt
import time

def on_mouse(event, x, y, flags, hsv):
    if event == cv.CV_EVENT_LBUTTONUP:
        print "(", y, ",", x, "):", hsv[y, x]

def main():
    # Read the .mp4 video using OpenCV Python API cv.VideoCapture

    cap = cv.VideoCapture("football_right.mp4")

   
    _,f = cap.read()
    
    #f = cv.imread("background.jpg", cv.CV_LOAD_IMAGE_COLOR)
    f_hsv = cv.cvtColor(f, cv.COLOR_BGR2HSV)
    cv.namedWindow('frame1')
    cv.SetMouseCallback('frame1', on_mouse, f_hsv)
    cv.imshow('frame1', f)
    cv.waitKey(0)
    
    
    
    cap.release()

main()
print ("Done!")
