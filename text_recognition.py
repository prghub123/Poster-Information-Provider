import os
import sys
import csv
import boto3

#Creates Class that initializes AWS boto3 client; Functionality includes
#opening an image and extracting text info in the image
class text_recognition():

    #retreving access key and password for AWS
    def __init__(self):
        with open('credentials.csv', 'r') as input:
            next(input)
            reader = csv.reader(input)
            for line in reader:
                access_key = line[2]
                password = line[3]
        #creating boto3 client
        boto3_client = boto3.client('rekognition', aws_access_key_id = access_key, aws_secret_access_key = password, region_name = 'us-west-2')
        self.img = []
        self.bytes = []

    #opening image and converting to byte64 format
    def open_img(image):
        self.img = image #pass in image here
        with open(img, 'rb') as image:
            self.bytes = image.read()

    def extract_text():
        #invokes AWS detect_text function to extract a dictionary with the text
        text = boto3_client.detect_text(Image = {'Bytes' : self.bytes})
        return text 
