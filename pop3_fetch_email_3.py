#!/usr/bin/python3

##
# Fetches emails from a server using pop3-ssl
# Python 3.5.2 version
#
##

# the cvt script was adjusted slightly
import poplib, datetime, ssl, logging
from cvt_pull_opp_mail import *

class Fetcher(object):

	def __init__(self):
		self.server = ""
		self.port = 995 
		self.user = ""
		self.password = ""

	def getemails(self):

		# context is only in python3.2+, defaults are: PROTOCOL_TLS, OP_NO_SSLv2, OP_NO_SSLv3 (most secure version)  
		context = ssl.create_default_context()
		try:
                	mailman = poplib.POP3_SSL(self.server, port=self.port, context=context)
                	mailman.user(self.user)
                	mailman.pass_(self.password)
		except poplib.error_proto as e:
                	logging.error("Poplib connection error: {}".format(e))

		numMsgs = len(mailman.list()[1])
		for index in range(numMsgs):
			msg=""
			for line in mailman.retr(index+1)[1]:
				msg += line.decode("utf-8", "ignore") + "\n"	
			try:
				# tests the decoding attachment script gets called correctly, using sample email in MIME format
				transformer = Transformer()
				print(transformer.perform(msg))

			except IOError as e:
				logging.error("Error writing to file: {}".format(e))	
		
		mailman.quit() 	

fetcher = Fetcher()
fetcher.getemails()

