# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:21:09 2019

@author: agirl
"""

import cv2
import numpy as np
pic=cv2.imread("tri.png")
cols=pic.shape[1]
rows=pic.shape[0]
H=np.float32([[1,0,150],[0,1,70]])
shifted=cv2.warpAffine(pic,H,(cols,rows))
cv2.imshow('shifted',shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()

#output=the image will be shifted to down right if  negative values are added then the images moves to left.