import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time


def scanned():
	cap = cv2.VideoCapture(0)

	cap.set(3,640)
	cap.set(4,480)
	while(cap.isOpened()):
	    # Capture frame-by-frame
	    ret, frame = cap.read()
	    # Our operations on the frame come here
	    im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    obj = pyzbar.decode(im)
	    if obj:
	    	break
	obj = obj[0]
	print(obj.data)
	return obj.data
        
               


