#!/usr/bin/env python3
import paramiko
import time
import sys

try:
	host = sys.argv[1]
	user = sys.argv[2]
	xattr_file = sys.argv[3]
except:
	print("Usage: ./xattr_timing.py host user /path/to/xattr/file")
	sys.exit(1)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, 22, user, '')

start = time.time()
stdin, stdout, stderr = ssh.exec_command('xattr -l ' + xattr_file)
end = time.time()
print(str(end-start)+"s")
print("Output: ")
for line in stdout.readlines():
	print(line)

print("Error: ")
for line in stderr.readlines():
	print(line)
