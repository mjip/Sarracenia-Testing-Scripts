#!/usr/bin/python3

##
#
# Gets new files from AWS S3 bucket.  
#
# 
#
#
##

import urllib.request,datetime,boto3
from botocore import UNSIGNED
from botocore.client import Config

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

# Gets the list of active weather station ICAOs from https://www.aviationweather.gov/docs/metar/stations.txt 
# According to the website's disclaimer:
#               " This server is available 24 hours a day, seven days a week. 
#                 Timely delivery of data and products from this server through the Internet is not guaranteed."
# Considered the primary resource for up-to-date ICAO information.
# Currently only scrapes US weather station ICAOs, but can be adjusted to pull from Canada/worldwide sites.
ICAOs = set()
with urllib.request.urlopen('https://www.aviationweather.gov/docs/metar/stations.txt') as f:
	lines = f.readlines()
	for line in lines:
		line = line.decode("utf-8","ignore")
		if len(line) > 80:
			if line.endswith("US\n") and line[65] == 'X':
				if line[20:24] != "    ": ICAOs.add(line[20:24])

# Not all sites from the Nexrad data set are covered from the official source 
#(some foreign US bases are included in the NEXRAD dataset), so add the missing ones from this list: 
# https://www.roc.noaa.gov/WSR88D/Program/NetworkSites.aspx
NOAA_ICAOs = ['RKJK','PAEC','RODN','RKSG','KGRK']
ICAOs.update(NOAA_ICAOs)

# And for some reason FOP1/NOP4 show up in the dataset, doesn't correlate to active ICAOs though
ICAOs.update(['FOP1','NOP4'])
# As of 2018/07 this set has 161 elements

# Takes all files uploaded on the specified day. Takes 161 API calls = ~9s. A full day's worth 
# of keys is around ~37000. Meant to be run once to grab a day's worth of keys. As long as a 
# day's worth on a single ICAO doesn't exceed 1000 (the API limit, and as of 2018/07 each ICAO
# uploads about ~300


now = datetime.datetime.utcnow()

YYYY = str(now.year)
MM = str(now.month).zfill(2)
DD = str(now.day).zfill(2)
HH = str(now.hour).zfill(2)
mm = str(now.minute).zfill(2)
ss = str(now.second).zfill(2)

for station in ICAOs:
	try:
		for obj in s3.list_objects(Bucket='noaa-nexrad-level2',Prefix=YYYY+'/'+MM+'/'+DD+'/'+station+'/')['Contents']:
			print(obj['Key'])
			print(obj['Size'])
	except KeyError as e:
		continue

# Forces sleep value to be a minute (could also be modified to be 1H or 10m). 
# Precise and fast (~9s), though kind of hack-y. Meant to be run continuously, in a polling program
"""
now = datetime.datetime.utcnow()

sleep = 60
for station in ICAOs:
	inc_now = now + datetime.timedelta(seconds=-sleep)
	YYYY = str(inc_now.year)
	MM = str(inc_now.month).zfill(2)
	DD = str(inc_now.day).zfill(2)
	HH = str(inc_now.hour).zfill(2)
	mm = str(inc_now.minute).zfill(2)
	try:
		for obj in s3.list_objects(Bucket='noaa-nexrad-level2',Prefix=YYYY+'/'+MM+'/'+DD+'/'+station+'/'+station+YYYY+MM+DD+'_'+HH+mm)['Contents']:
			print(obj['Key'])
	except KeyError as e:
		continue
"""
# Checks for files uploaded since it last went to sleep, takes around O(sleep * 161) API calls 
#(which are slow, to the order of a couple dozen minutes).
"""now = datetime.datetime.utcnow()

sleep = 600
inc = -sleep
for station in ICAOs:
        while inc <= 0:
                inc_now = now + datetime.timedelta(seconds=inc)
                YYYY = str(inc_now.year)
                MM = str(inc_now.month).zfill(2)
                DD = str(inc_now.day).zfill(2)
                HH = str(inc_now.hour).zfill(2)
                mm = str(inc_now.minute).zfill(2)
                ss = str(inc_now.second).zfill(2)
                try:
                        for obj in s3.list_objects(Bucket='noaa-nexrad-level2',Prefix=YYYY+'/'+MM+'/'+DD+'/'+station+'/'+station+YYYY+MM+DD+'_'+HH+mm+ss)['Contents']:
                                print(obj['Key'])
                except KeyError as e:
                        inc+=1
                        continue

                inc+=1
        inc = -sleep
"""

# Tries to find all the keys using http response codes. Probably slowest method of all.
"""
now = datetime.datetime.utcnow()

YYYY = str(now.year)
MM = str(now.month).zfill(2)
DD = str(now.day).zfill(2)
HH = str(now.hour).zfill(2)
mm = str(now.minute).zfill(2)
ss = str(now.second).zfill(2)

sleep = 600
inc = -sleep
for station in ICAOs:
	while inc <= 0:
		inc_now = now + datetime.timedelta(seconds=inc)
		YYYY = str(inc_now.year)
		MM = str(inc_now.month).zfill(2)
		DD = str(inc_now.day).zfill(2)
		HH = str(inc_now.hour).zfill(2)
		mm = str(inc_now.minute).zfill(2)
		ss = str(inc_now.second).zfill(2)
		buildurl = "https://s3.amazonaws.com/noaa-nexrad-level2/"+YYYY+'/'+MM+'/'+DD+'/'+station+'/'+station+YYYY+MM+DD+'_'+HH+mm+ss+'_'+'V06'
		try:
			if urllib.request.urlopen(buildurl).getcode() == 200:
				print(buildurl)
		except:
			continue
"""			
