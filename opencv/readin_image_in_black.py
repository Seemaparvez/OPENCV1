import numpy as np
import cv2 as cv 
img=cv.imread('tri.jpg',0)
cv.imshow('Original',img)
cv.waitKey(0)

cv.destroyAllWindows()
