#!/usr/bin/python

"""
\file tracker_tc.py

@brief tracker code for performing mean shift tracking

@author Mathew Francis

@date 12/06/2017

"""

# import the necessary packages
import sys
import time
import cv2
import numpy as np
import collections
import math
import glob
from time import time
import os
import shutil


from sklearn.feature_extraction.image import extract_patches_2d
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.preprocessing import normalize
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import orthogonal_mp
from sklearn import svm


from numpy import linalg as LA




# import the packages for logging 
import logging
import logging.handlers
import logging.config



# import the user defined packages
import Parameters
import meanshifttracking




#========================================================================================================================#

# log configuration file
logging.config.fileConfig('logging.conf')

# Defining the logger
logger = logging.getLogger("tracker")

# writing into the log file
logger.info("Program started")




# parameter object filename.class name
params = Parameters.Parameters()  

# Invoking the constructor to initialize the tracker parameters
#tracker = PTracker.PTracker( params )





centroid_x = int(( sum( params._ground_truth[0][0:8:2] ) * 0.25 ))

centroid_y = int(( sum( params._ground_truth[0][1:8:2] ) * 0.25 ))

min_x = min( params._ground_truth[0][0:8:2] )
min_y = min( params._ground_truth[0][1:8:2] )

max_x = max( params._ground_truth[0][0:8:2] )
max_y = max( params._ground_truth[0][1:8:2] )     


obj_width = max_x - min_x
obj_height = max_y -min_y

tracker = meanshifttracking.MeanShiftTracker( centroid_x , centroid_y , obj_width , obj_height )



ref_image = curr_img_color =  cv2.imread( params._image_name_list [ 0 ]   )

# initialize the tracker
tracker.compute_target_model(  ref_image  )

cv2.namedWindow('img')

    
for i in range( 1, len( params._image_name_list) , 1):
    
    # read current frame
    image = curr_img_color =  cv2.imread( params._image_name_list [ i ]   )
    
    tracker.perform_mean_shift( image )
  
    
    x1 = tracker._curr_centroid_x - tracker._curr_half_width
    y1 = tracker._curr_centroid_y - tracker._curr_half_height
    

    x2 = tracker._curr_centroid_x + tracker._curr_half_width
    y2 = tracker._curr_centroid_y + tracker._curr_half_height    
    
    
    cv2.rectangle( image , (x1, y1), (x2, y2), (255,0,0), 2)
    cv2.imshow( 'img', image )
    cv2.waitKey( 50 )


