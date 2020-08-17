import numpy as np  
import matplotlib.pyplot as plt
import numpy as np
import cv2
import skimage.viewer
img=cv2.imread('dino1.png')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2 = cv2.threshold(grayscaled,140,255,cv2.THRESH_BINARY)
viewer = skimage.viewer.ImageViewer(threshold2)
viewer.show()