#!/usr/bin/python2
#coding=utf-8
import RPi.GPIO as GPIO
import time
import math
GPIO.setmode(GPIO.BOARD)
class led:
	def __init__(self):
		GPIO.setup(7,GPIO.OUT)
		GPIO.setup(11,GPIO.OUT)
		# GPIO.output(7,GPIO.HIGH)
		# GPIO.output(11,GPIO.HIGH)
		GPIO.setup(13,GPIO.OUT)
		GPIO.setup(15,GPIO.OUT)
		# GPIO.output(13,GPIO.HIGH)
		# GPIO.output(15,GPIO.HIGH)
		self.p=GPIO.PWM(7,1500)
		self.s=GPIO.PWM(13,1500)
	def light(self,dc):
		if dc<=0 or dc > 100:
			GPIO.output(7,GPIO.LOW)
			GPIO.output(11,GPIO.LOW)
			return "close"
		else:
			# GPIO.output(7,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			self.p.start(dc)
			return "open"
	def left(self,dc):
		if dc<=0 or dc > 100:
			GPIO.output(13,GPIO.LOW)
			GPIO.output(15,GPIO.LOW)
			return "close"
		else:
			# GPIO.output(13,GPIO.HIGH)
			GPIO.output(15,GPIO.HIGH)
			self.s.start(dc)
			return "open"
	def close(self):
		if GPIO.cleanup==None:
			pass
		else:
			GPIO.cleanup()
if(__name__=='__main__'):
	pass
