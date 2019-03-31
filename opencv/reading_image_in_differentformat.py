#image in different format
import numpy as np
import cv2 as cv 
img=cv.imread('tri.jpg')
img=cv.imwrite('tri.png',img)
cv.imshow('Original',img)
cv.waitKey(0)

cv.destroyAllWindows()
