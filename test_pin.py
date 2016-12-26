#!/usr/bin/python

import RPi.GPIO as GPIO

pin = 17
print 'momega'
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(pin,OUTPUT)
GPIO.output(pin,GPIO.HIGH)
raw_input('press enter')
GPIO.cleanup()
