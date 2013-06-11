#!/usr/bin/python
 
import RPi.GPIO as GPIO
import time
 
IO_NO = 0
 
print("press ^C to exit program ...\n")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN) 
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(IO_NO, GPIO.IN)
 
for n in range(20):
	#print GPIO.input(IO_NO)
	print GPIO.input(3)
	time.sleep(1)
print "end"
"""
try:
 while True:
  print(GPIO.input(IO_NO))
  time.sleep(1)
except KeyboardInterrupt:
 print("detect key interrupt\n")
 
"""
GPIO.cleanup()
print("Program exit\n")
