# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:50:44 2019

@author: agirl

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=np.zeros((50,50),np.uint8)


img[20:25,0:50]=5
plt.imshow(img,cmap='Greys_r')

filter1=np.array([[1,1,1],[0,0,0],[1,1,1]])

H=cv2.filter2D(img,-1,filter1)
plt.imshow(H,  cmap='Greys_r')