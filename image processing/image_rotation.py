# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:34:06 2019

@author: agirl
"""

import cv2
#import numpy as np
pic=cv2.imread('tri.jpg')
rows=pic.shape[1]
cols=pic.shape[0]
center=(cols/2,rows/2)
angle=90
H=cv2.getRotationMatrix2D(center,angle,1)
rotate=cv2.warpAffine(pic,H,(cols,rows))
cv2.imshow('rotated',rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
