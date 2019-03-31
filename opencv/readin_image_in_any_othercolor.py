import numpy as np
import cv2 as cv 
img=cv.imread('tri.jpg',140)#0-255 any random color
cv.imshow('Original',img)
cv.waitKey(0)

cv.destroyAllWindows()
