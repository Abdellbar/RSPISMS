#!/usr/bin/env python


import time
from pygsm import GsmModem
import RPi.GPIO as GPIO

#set pin12 to output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

class SwitchLED(object):
	def __init__(self, modem):
		self.modem = modem

	def incoming(self, msg):
		if msg=="on":
			GPIO.output(12, GPIO.HIGH) #switch on the led
		elif msg=="off":
			GPIO.output(12, GPIO.LOW) #switch off the led
		else:
			msg.respond("worong comande use on or off")

	def serve_forever(self):
		while True:
			print "Checking for message..."
			msg = self.modem.next_message()

			if msg is not None:
				print "Got Message: %r" % (msg)
				self.incoming(msg)

			time.sleep(2)


DRIVER="/dev/ttyUSB0"

gsm = GsmModem(port=DRIVER,baudrate=115200,logger=GsmModem.debug_logger).boot()

print "Waiting for network..."
s = gsm.wait_for_network()

# demo
app = SwitchLED(gsm)
app.serve_forever()