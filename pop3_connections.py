#!/usr/bin/python3

import poplib, datetime, ssl, os, time, sys

try:
	context = ssl.create_default_context()
	mailman = poplib.POP3_SSL("", port=995, context=context)
	mailman.user("")
	mailman.pass_("")
except poplib.error_proto as e:
    print("Poplib connection error: {}".format(e))

try:
	while True:
		print("Connection open, id: ", os.getpid())
		time.sleep(40) # sleep 40s	
except KeyboardInterrupt:
	mailman.quit()
	print("Connection successfully closed.")
	sys.exit(0)

mailman.quit() 	

