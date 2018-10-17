#!/usr/bin/python3

import time,string,itertools,pprint

#find all dddddd combinations 
start = time.time()
digs = list(string.digits)
lst = list(itertools.product(digs,repeat=6))
end = time.time()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(lst)
print("It took {} s.".format(end-start))

