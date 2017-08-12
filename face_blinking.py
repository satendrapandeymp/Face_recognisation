import numpy as np, urllib2, time
import cv2

#For connecting with droidcam
testVar = raw_input("Enter the Ip of your phone (Droidcam only) like 192.168.1.100 \n")
cam = "http://" + testVar + ":4747/mjpegfeed?640x480"

cap = cv2.VideoCapture(0)

# Inter location  of haarcascade_frontalface_default.xml from your computor
face_cascade = cv2.CascadeClassifier('/home/pandey/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')  

while(True):
	ret, img = cap.read()
	if ret is True:
		flag = 0
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			if (flag == 0):
				link = "http://" + testVar + ":4747/cam/1/led_toggle"
				#urllib2.urlopen(link).read()    # This will gonna turn on the led
				flag = 1
				name = "Temp/" + str(time.time()) + ".jpg"
				cv2.imwrite(name, img) 
				#urllib2.urlopen(link).read()   # this will gonna turn off the led
	else:
		print "Can't read Frames"
				

				

