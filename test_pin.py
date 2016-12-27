#!/usr/bin/python

import RPi.GPIO as GPIO
import time

pin = 17
print 'momega'
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(pin,GPIO.OUT)


GPIO.output(pin,GPIO.HIGH)
time.sleep(2)
GPIO.output(pin,GPIO.LOW)
time.sleep(2)
GPIO.output(pin,GPIO.HIGH)
time.sleep(2)
GPIO.output(pin,GPIO.LOW)
time.sleep(2)
GPIO.output(pin,GPIO.HIGH)

raw_input('press enter')
GPIO.cleanup()
