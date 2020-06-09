import os
import sys
import csv
import boto3

#Creates Class that initializes AWS boto3 client; Functionality includes
#opening an image and extracting text info in the image
class text_recog:

    #retreving access key and password for AWS
    def __init__(self):
        with open('rootkey.txt', 'r') as input:
            lines = input.readlines() #creates list of lines in the txt file
            access_key = lines[0]
            password = lines[1]
            access_key = access_key.replace('\n', '') #remove new line character from access_key
        #creating boto3 client
        self.boto3_client = boto3.client('rekognition', aws_access_key_id = access_key, aws_secret_access_key = password, region_name = 'us-west-2')
        self.img = []
        self.bytes = []

    #opening image and converting to byte64 format
    def open_img(self, image):
        self.img = image #pass in image here
        with open(self.img, 'rb') as image:
            self.bytes = image.read()

    #invokes AWS detect_text function to extract a dictionary with the text
    def extract_text(self):
        #calls boto3 detect_text method (returns a dictonary)
        text = self.boto3_client.detect_text(Image = {'Bytes' : self.bytes})
        #returns a list of text detected
        words = text['TextDetections']
        return words
