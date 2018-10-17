#!/usr/bin/python3

import ftplib
import sys
import time

# usage: ./test_ftplib.py user password host
# to deal with empty passwords
class MainClass():
	def ls_file_index(self,iline):
		oline = iline
		oline = oline.strip('\n')
		oline = oline.strip()
		oline = oline.replace('\t',' ')
		opart1 = oline.split(' ')
		opart2 = []
		for p in opart1:
			if p == '': continue
			opart2.append(p)

		try:
			file_index = opart2.index(self.init_nlst[self.init_nlst_index])
			self.file_index = file_index
		except:
			pass
		finally:
			self.init_nlst_index += 1

	def start(self):
		if len(sys.argv) == 3:
			arg1 = sys.argv[1]
			arg2 = ''
			arg3 = sys.argv[2]
			arg4 = 21
		elif len(sys.argv) == 5:
			arg1 = sys.argv[1]
			arg2 = sys.argv[2]
			arg3 = sys.argv[3]
			arg4 = sys.argv[4]
		else:
			arg1 = sys.argv[1]
			arg2 = sys.argv[2]
			arg3 = sys.argv[3]
			arg4 = 21
	
		ftp = ftplib.FTP()
		try:
			ftp.connect(arg3, port=int(arg4))
			ftp.login(arg1,arg2)
		
			start = time.time()
			#server_help = ftp.sendcmd('HELP')
			self.init_nlst = sorted(ftp.nlst())
			self.init_nlst_index = 0
			self.file_index = -1
			ftp.retrlines('LIST', self.ls_file_index )
			if self.file_index == -1:
				self.empty_ls = True
			print(self.file_index)
			#print(server_help)
			end = time.time()
			print(str(end-start))
		finally:
			ftp.quit()

if __name__ == "__main__":
	a = MainClass()
	a.start()
