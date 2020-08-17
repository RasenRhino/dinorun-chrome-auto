import cv2
import numpy as np

def on_click(event, x, y, p1, p2):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
img=cv2.imread('dino1.png')
#g2=cv2.cvtColor(find,cv2.COLOR_BGR2GRAY)
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2 = cv2.threshold(grayscaled,70,255,cv2.THRESH_OTSU)
# retval2,threshold3 = cv2.threshold(g2,70,255,cv2.THRESH_BINARY_INV)
cv2.imshow('gg',threshold2)
cv2.namedWindow('gg')
# cv2.imshow('g2',threshold2)
print(threshold2.shape)
cv2.setMouseCallback('gg', on_click)


cv2.waitKey(0)
cv2.destroyAllWindows()