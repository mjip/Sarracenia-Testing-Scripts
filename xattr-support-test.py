#!/usr/bin/env python3

import xattr

try:
	xattr.setxattr("/tmp/test.txt","user.comment",b"test comment")
	print(xattr.getxattr("/tmp/test.txt", "user.comment"))

except Exception as e:
	print("Exception: {}".format(e))
	print("Type: {}".format(type(e)))
