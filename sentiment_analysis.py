import os
import sys
import csv
from text_recognition import text_recog
import boto3

#doing some testing 
test = text_recog();
test.open_img('blueberries.jpg')
text = test.extract_text()
print(text.keys())
