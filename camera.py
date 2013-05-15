#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013/05/13

@author: Yohei Kinowaki

カメラ画像の取得および保存

'''
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
        while True:
            img = cv.QueryFrame(self.capture)
            #cv.ShowImage("camera", img)
            cv.SaveImage("OutImage.jpg",img)
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
    
