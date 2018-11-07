#!/usr/bin/python3

import time,string,itertools,pprint

#find all XXXX combinations 
start = time.time()
caps = list(string.ascii_uppercase)
#lst = ['{}{}{}{}'.format(a,b,c,d) for a,b,c,d in caps,caps,caps,caps]
lst = list(itertools.product(caps,repeat=4))
end = time.time()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(lst)
print("It took {} s.".format(end-start))
