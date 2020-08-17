import cv2
import numpy as np
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        # cv2.circle(threshold2,(x,y),10,(150,150,150),-1)
        # cax=x+10
        # print(x,y)
        # print(threshold2[x][y])
        # for i in range(cax,threshold2.shape[0]):
        # 	if(threshold2[i][y]==0):
        # 		cv2.circle(threshold2,(i,y),5,(150,150,150),-1)
        		

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
img=cv2.imread('dino1.png')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2 = cv2.threshold(grayscaled,140,255,cv2.THRESH_BINARY)
print(np.unique(threshold2))
while True:
	cv2.imshow('image',threshold2)
	if cv2.waitKey(20) == 27:
		break
cv2.destroyAllWindows()

# https://answers.opencv.org/question/94845/python-opencv-extracting-xy-coordinates-of-point-features-on-an-image/
# check this out