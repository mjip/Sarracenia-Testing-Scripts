#!/usr/bin/python3

from boto3 import client
from botocore import UNSIGNED
from botocore.client import Config

conn = client('s3', region_name='us-east-1', config=Config(signature_version=UNSIGNED, retries={'max_attempts':3}))
bucket = conn.list_objects(Bucket='noaa-goes16')['Contents']
for obj in bucket:
	print(obj['Key'])
