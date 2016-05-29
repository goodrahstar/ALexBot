# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:16:37 2016

@author: rahul_z_kuma
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) 
# choose the pin numbering
GPIO.setup(12, GPIO.OUT)


GPIO.output(12, 0)
print 'Button Pressed'

time.sleep(7)
GPIO.output(12,1)

print "Button Released"

GPIO.cleanup()
