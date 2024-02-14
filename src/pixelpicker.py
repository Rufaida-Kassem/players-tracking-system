import numpy as np
np.set_printoptions(threshold=np.nan)
import numpy.linalg as la
import cv2 as cv
# import cv2 as cv.cv as cv
import math
import matplotlib.pyplot as plt
import time

# Count runtime

start_time = time.time()
vid_filepath = '..//vid//panorama.mov'
def on_mouse(event, x, y, flags, param):
    if event == cv.CV_EVENT_LBUTTONUP:
        print ("col: %d, row: %d" % (x, y))

def main():
    # Read the .mp4 video using OpenCV Python API cv.VideoCapture

    vid_cap = cv.VideoCapture(vid_filepath)

    # Print the frame width, frame height, frames per second 
    # and frame count of the input video using cap.get

    fwidth = vid_cap.get(cv.CV_CAP_PROP_FRAME_WIDTH)
    fheight = vid_cap.get(cv.CV_CAP_PROP_FRAME_HEIGHT)
    fps = vid_cap.get(cv.CV_CAP_PROP_FPS)
    fcount = vid_cap.get(cv.CV_CAP_PROP_FRAME_COUNT)

    print ("Frame width: " + str(fwidth) + "\nFrame height: " + str(fheight) + "\nFrames per second: " + str(fps) + "\nFrame count: " + str(fcount))

    _,img = vid_cap.read()
    filename_topview = '..//img//top-view.jpg'
    
    top_image = cv.imread(filename_topview)
    
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.namedWindow('frame1')
    cv.SetMouseCallback('frame1', on_mouse, None)
    cv.imshow('frame1', top_image)
    cv.waitKey(0)
    
    
    
    vid_cap.release()

main()
print("Done! Took %s seconds" % (time.time() - start_time))
