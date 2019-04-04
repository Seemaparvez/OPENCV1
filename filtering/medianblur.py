# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:48:39 2019

@author: agirl
"""

import cv2
#import numpy
pic=cv2.imread("tri.png")
k=3
median=cv2.medianBlur(pic,k)
cv2.imshow('median',pic)
cv2.waitKey(0)
cv2.destroAllWindows()
