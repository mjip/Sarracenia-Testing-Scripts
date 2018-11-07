#!/usr/bin/python3

import paramiko
import sys

# usage: ./sftp_xattr.py user host path

try:
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]
	arg3 = sys.argv[3]
except:
	print("Usage_ ./sftp_xattr.py user host path")
	sys.exit(0)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(arg2, 22, arg1, '')
sftp = ssh.open_sftp()

sftp.chdir(arg3)

ldir = sftp.listdir()
for index in range(len(ldir)):
	print("Attributes: {}".format(sftp.stat(ldir[index]).attr))

sftp.close()
