import cv2
import numpy as np
#img1 = cv2.imread('mainsvm.png')
img2 = cv2.imread('Untitled.png')
row,column,channel=img2.shape
# roi=img1[0:row,0:column]
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mas=cv2.threshold(img2gray,255,0,cv2.THRESH_BINARY_INV)
mas_inv=cv2.bitwise_not(mas)
#imgbg=cv2.bitwise_and(roi,roi,mask=mas_inv)
imgfg=cv2.bitwise_and(img2,img2,mask=mas)
#cv2.imshow("1",imgbg)
cv2.imshow("2",imgfg)
# out=cv2.add(imgfg,imgbg)
# img1[0:row,0:column]=out;
# cv2.imshow("3",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()