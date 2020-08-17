import cv2
import numpy as np
import pyautogui
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

st=time.time()
while True:
	if((time.time()-st)>2):
		break
while True:
	# make a screenshot
	img = pyautogui.screenshot()
	# convert these pixels to a proper numpy array to work with OpenCV
	frame = np.array(img)
	grayscaled = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(grayscaled,140,255,cv2.THRESH_BINARY)
	for i in range(540,1080):
		if thresh[i,300]==0:
			if(i<690):
				print(i)
				keyboard.press(Key.space)                                      
				break
			else:
				break                          
	# cv2.imshow('lol',thresh)            
	# if the user clicks q, it exits
	if cv2.waitKey(1) == ord("q"):                      
		break
	            
