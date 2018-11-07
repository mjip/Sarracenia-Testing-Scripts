#!/usr/bin/python3

import poplib, imaplib, sys

server = ""
port = 993
user = ""
password = ""

if sys.argv[1] == "pop":
	try:
		mailman = poplib.POP3_SSL(server, port=port)
		mailman.user(user)
		mailman.pass_(password)
	except poplib.error_proto as e:
		print("poplib connection error bruh {}".format(e))

	numMsgs = len(mailman.list()[1])
	for index in range(numMsgs):
		msg=""
		for line in mailman.retr(index+1)[1]:
			msg += line.decode("utf-8","ignore") + "\n"
		mailman.dele(index+1)
	mailman.quit()
	print("Msg should've gotten deleted asdflkajsdf")

elif sys.argv[1] == "imap":
	try:
		mailman = imaplib.IMAP4_SSL(server, port=port)
		mailman.login(user,password)
	except imaplib.IMAP4.error as e:
		print("imaplib connection error bruh {}".format(e))

	mailman.select(mailbox='INBOX')
	resp, data = mailman.search(None, 'ALL')
	for index in data[0].split():
		r, d = mailman.fetch(index, '(RFC822)')
		msg = d[0][1].decode("utf-8", "ignore") + "\n"
		mailman.store(index, '+FLAGS', '\\Deleted')

	mailman.expunge()
	mailman.close()
	mailman.logout()
	print("Msg should've gotten deleted sadfkalsdg")
else:
	print("try again nerd")
