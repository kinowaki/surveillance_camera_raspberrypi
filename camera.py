#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2013/05/13

@author: Yohei Kinowaki

カメラ画像の取得および保存

'''
import RPi.GPIO as GPIO
import cv
import time
import os
print os.getcwd()


class Camera:

    def __init__(self):
        
        #cv.NamedWindow("camera", 1)
        self.capture = cv.CreateCameraCapture(0)

        width = None #leave None for auto-detection
        height = None #leave None for auto-detection

        if width is None:
            width = int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_WIDTH))
        else:
                cv.SetCaptureProperty(self.capture,cv.CV_CAP_PROP_FRAME_WIDTH,width)    

        if height is None:
                height = int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
        else:
                cv.SetCaptureProperty(self.capture,cv.CV_CAP_PROP_FRAME_HEIGHT,height) 
    def run(self):
	IO_NO = 0
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3, GPIO.IN)
        while True:
            img = cv.QueryFrame(self.capture)
            #cv.ShowImage("camera", img)
	    input = GPIO.input(3)
	    input = 0
            if input == 0:
		GPIO.cleanup()
            	cv.SaveImage("OutImage.jpg",img)
	    	print "end"
		break
	    c = cv.WaitKey(1);
            if c == 27:
                break
            elif c == ord("f"):
                break
            elif c == ord("g"):
                cv.SaveImage("OutImage.jpg",img)
                print "ok"
                #cv.DestroyWindow("camera")
                break
                
    
if __name__=="__main__":
    camera = Camera()
    camera.run()
    
