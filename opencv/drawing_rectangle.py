#rectangle
import numpy as np
import cv2 as cv
pic=np.zeros((500,500,30),dtype='uint8')

cv.rectangle(pic,(0,0),(500,50),(125,200,90),3,lineType=0,shift=0)
cv.imshow('pic',pic)
cv.waitKey(0)
cv.destroyAllWindows()
