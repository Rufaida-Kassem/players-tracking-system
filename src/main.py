import numpy as np
#np.set_printoptions(threshold=np.nan)
# use sys.maxsize to print the entire array
# np.set_printoptions(threshold=np.sys.maxsize)
import numpy.linalg as la
import os
import os.path

import cv2 as cv
# # import cv2 as cv.cv as cv
import math
import matplotlib.pyplot as plt
import time
import bgextraction
import topview
import playertrack

bg_filpath = '..//img//side-view.jpg'
vid_filepath = '..//vid//panorama.mov'
hgmatrix_filepath = '..//txt//hgmatrix.txt'

def main():
	if(not os.path.isfile(bg_filpath)):
		if(not os.path.exists('..//img')):
			os.mkdir('..//img')
		print ("Background has not been extracted, will extract.")
		bgextraction.extract_background(vid_filepath)
	bg_img = cv.imread(bg_filpath)
	print ("Background image found")

	if(not os.path.isfile(hgmatrix_filepath)):
		if(not os.path.exists('..//txt')):
			os.mkdir('..//txt')
		print ("Homography matrix has not been created.")
		topview.create_homography()
	hg_matrix = np.loadtxt(hgmatrix_filepath)
	print ("Homography matrix found")
	print (hg_matrix)
	
	playertrack.track_player(hg_matrix)
	
main()