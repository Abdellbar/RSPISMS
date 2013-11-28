#!/usr/bin/env python
from pygsm import GsmModem

class GsmModule(object):
	def __init__(self, modem):
		self.modem = modem

	def sendsms(self):
		print "sending sms"
		msg="salam raspberry :)"
		self.modem.send_sms(+212661242524,msg)
		print "sms sent"


DRIVER="/dev/ttyUSB0"

print "hello Raspberry"
gsm = GsmModem(port=DRIVER,baudrate=115200,logger=GsmModem.debug_logger).boot()
print "Waiting for network..."
s = gsm.wait_for_network()

#demo
app = GsmModule(gsm)
print "sending ..."
app.sendsms() 