import os
import sys
import csv
import boto3
from text_analysis import text_analysis
from googlesearch import google
"""
analysis = text_analysis()
text = analysis.recognize_text('blueberries.jpg')
theblob = analysis.filter_words(text)
analysis.sentiment(theblob)
process_blob = analysis.preprocess(theblob)
print(process_blob.words)"""

class websearch():
    
