#!/usr/bin/python3

import imaplib, datetime, ssl, os, time, sys

context = ssl.create_default_context()
try:
	mailman = imaplib.IMAP4_SSL("", port=993, ssl_context=context)
	mailman.login("", "")
	mailman.select('INBOX')
except ConnectionResetError:
	print("Connection reset")

try:
	while True:
		print("Connection open, id: ", os.getpid())
		time.sleep(40) # sleep 40s	
except KeyboardInterrupt:
	mailman.close()
	mailman.logout()
	print("Connection successfully closed.")
	sys.exit(0)

mailman.close()
mailman.logout()

