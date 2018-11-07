#!/usr/bin/python3

import datetime
import time

debian_unstable1 = ['-rw-r--r--','1','wooledg','wooledg','240','2007-12-07','11:44','file1']
debian_unstable2 = ['-rw-r--r--','1','wooledg','wooledg','240','2007-12-07','11:44','file1','with','spaces']
open_bsd1 = ['-rwxr-xr-x ','1','greg','greg','80','Nov','10','2006','file1']
open_bsd2 = ['-rw-r--r--','1','greg','greg','1020','Mar','15','13:57','file2']
open_bsd3 = ['-rw-r--r--','1','greg','greg','1020','Mar','15','13:57','file2','with','spaces']
open_bsd4 = ['-rw-r--r--','1','greg','greg','1020','Jan','1','2000','file3','with','spaces']

listings = [debian_unstable1,debian_unstable2,open_bsd1,open_bsd2,open_bsd3,open_bsd4]

# looking for first appearance of datetime like object in list
# if ls timestamp format is non-standard, just assume the ftp server admin
# has a heart and doesn't create directories with spaces in the name, and take [-1]

for lst in listings:
	start = time.time()
	fichier = ''
	index = -1
	not_parsed = True
	while not_parsed:
		if index < -len(lst):
			# non-standard timestamp, take -1
			fichier = lst[-1]
			not_parsed = False
		else:
			try: 
				datetime.datetime.strptime(lst[index],'%H:%M')
				fichier = lst[index+1:]
				not_parsed = False
			except:
				try:
					datetime.datetime.strptime(lst[index],'%Y')
					fichier = lst[index+1:]
					not_parsed = False
				except:
					index-=1
					pass
	

	end = time.time()
	fil = ' '.join(fichier)
	print("listing: %s, filename: %s, time to get: %s" % (lst,fil,str(end-start)))
