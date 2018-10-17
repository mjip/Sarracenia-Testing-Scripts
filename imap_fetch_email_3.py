#!/usr/bin/python3

##
# Fetches emails from a server using imap-ssl
# Python 3.5.2 version
#
##

# the cvt script was adjusted slightly
import imaplib, datetime, ssl, logging
from cvt_pull_opp_mail import *

class Fetcher(object):
	
        def __init__(self):
                self.server = ""
                self.port = 993 # standard IMAP4-over-SSL port 
                self.user = ""
                self.password = ""

        def getemails(self):

                # context is only in python3.3+, defaults are: PROTOCOL_TLS, OP_NO_SSLv2, OP_NO_SSLv3 (most secure version)  
                context = ssl.create_default_context()
                try:
                        mailman = imaplib.IMAP4_SSL(self.server, port=self.port, ssl_context=context)
                        mailman.login(self.user, self.password)
                except imaplib.IMAP4.error as e:
                        logging.error("Imaplib connection error: {}".format(e))

                # only retrieves unread mail from inbox
                mailman.select(mailbox='INBOX')
                resp, data = mailman.search(None, '(UNSEEN)')
                for index in data[0].split():
                        r, d = mailman.fetch(index, '(RFC822)')
                        msg = d[0][1].decode("utf-8", "ignore") + "\n"
                
                        try:
                                # tests the decoding attachment script gets called correctly, using sample email in MIME format
                                transformer = Transformer()
                                print(transformer.perform(msg))
                        except IOError as e:
                                logging.error("Error writing to file: {}".format(e))
                mailman.close()
                mailman.logout()

fetcher = Fetcher()
fetcher.getemails()
