import cvlib as cv
import cv2
from cvlib.object_detection import draw_bbox
img=cv2.imread('dino_run.png')
bbox, label, conf = cv.detect_common_objects(img,enable_gpu=True)

output_image = draw_bbox(img, bbox, label, conf)
cv2.imshow('lol',output_image)
cv2.waitKey(0)