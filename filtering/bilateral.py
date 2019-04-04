# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:40:04 2019

@author: agirl
"""


import cv2
#import numpy
pic=cv2.imread("tri.png")
dimpixel=7
color=100
space=100
filter=cv2.bilateralFilter(pic,dimpixel,color,space)
cv2.imshow('filter',filter)
cv2.waitKey(0)
cv2.destroyAllWindows()