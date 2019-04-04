# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:46:40 2019

@author: agirl
"""

#canny edge detector
import cv2
#import numpy as np
pic=cv2.imread('tri.png')
thresholdval1=50
thresholdval2=150

canny=cv2.Canny(pic,thresholdval1,thresholdval2)
cv2.imshow('canny',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
