import os
import sys
import csv
import boto3

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key = line[2]
        password = line[3]
img = '' #pass in image here
#print(access_key)
#print(password)
boto3_client = boto3.client('rekognition', aws_access_key_id = access_key, aws_secret_access_key = password)
