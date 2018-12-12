#!/usr/bin/python3

from boto3 import client
from botocore import UNSIGNED
from botocore.client import Config
import datetime

conn = client('s3', region_name='us-east-1', config=Config(signature_version=UNSIGNED, retries={'max_attempts':3}))
bucket = conn.list_objects(Bucket='noaa-goes16')['Contents']

paginator = conn.get_paginator("list_objects")
page_iterator = paginator.paginate(Bucket='noaa-goes16')

for page in page_iterator:
	if 'Contents' in page:
		for key in page['Contents']:
			print(key['Key'])

#get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))

#filt_iterator = page_iterator.search("Contents[?LastModified >= `datetime.datetime(2018, 12, 11, 8, 5, 37, tzinfo=tzutc())`].Key")
#for key_data in filt_iterator:
#	print(key_data)

#print(max(enumerate(page_iterator))[1])

#bucket = conn.list_objects(Bucket='noaa-nexrad-level2')['Contents']
#bucket = [obj['Key'] for obj in sorted(bucket, key=get_last_modified)]
#for obj in bucket:
#	print(obj['Key'])
