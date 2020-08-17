import cv2
import numpy as np
from python_imagesearch.imagesearch import imagesearch
img=cv2.imread('dino_run.png')
find=cv2.imread('Untitled.png')
g2=cv2.cvtColor(find,cv2.COLOR_BGR2GRAY)
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2 = cv2.threshold(grayscaled,70,255,cv2.THRESH_OTSU)
retval2,threshold3 = cv2.threshold(g2,70,255,cv2.THRESH_BINARY_INV)
cv2.imshow('gg',threshold3)
cv2.imshow('g2',threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()