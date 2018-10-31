#!/usr/bin/env python3

import os
import time
import sys
import stat

try: fname = sys.argv[1]
except: 
	print("Usage: specify file to test file stats on as first arg")
	sys.exit(0)

start = time.time()

lstat = os.stat(fname)

end = time.time()
print("It took {0} to generate the stat of the file".format(end-start))

start = time.time()

mtime = lstat[stat.ST_MTIME]

end = time.time()
print("It took {0} to check the mtime of the file".format(end-start))

start = time.time()

fsiz = lstat[stat.ST_SIZE]

end = time.time()
print("It took {0} to check the size of the file".format(end-start))


