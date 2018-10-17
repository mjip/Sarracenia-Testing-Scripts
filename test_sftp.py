#!/usr/bin/python3

import paramiko
import time
import sys

# usage: ./test_sftp.py user password host
# to deal with empty passwords


class MainClass():

	def ls_file_index(self):
		pass	

	def start(self):
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		
		if len(sys.argv) == 3:
			arg1 = sys.argv[1]
			arg2 = ''
			arg3 = sys.argv[2]
			arg4 = 22
			try:
				ssh.connect(arg3,int(arg4),arg1,arg2)
			except:
				ssh.connect(arg3,int(arg4),arg1,arg2,allow_agent=False,look_for_keys=False)
		else:
			arg1 = sys.argv[1]
			arg2 = sys.argv[2]
			arg3 = sys.argv[3]
			try:
				arg4 = sys.argv[4]
			except:
				arg4 = 22
			ssh.connect(arg3,int(arg4),arg1,arg2,allow_agent=False,look_for_keys=False)
	
		sftp = ssh.open_sftp()
		try:
			# they aren't sorted, but they have the same order anyway
			dir_attr = sftp.listdir_attr()
			dir_fils = sftp.listdir()
			for index in range(len(dir_attr)):
				attr = dir_attr[index]
				print(attr.__str__())
				print(dir_fils[index])

		finally:
			sftp.close()
			ssh.close()

if __name__ == "__main__":
	a = MainClass()
	a.start()
