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

class websearch:
    #function invokes google search api to find web results
    def search_google(self):
        query = ' '.join(self.thewords)
        #use search function from google api to retrieve first 10 web results for the phrase searched
        results = search(query, tld='com', lang = 'en', num=10, start=0, end=10, pause=2)
        return results
    #function that executes text recognition and text_analysis
    def text_execution(self, pic_name):
        analysis = text_analysis()
        text = analysis.recognize_text(pic_name)
        theblob = analysis.filter_words(text)
        analysis.sentiment(theblob)
        process_blob = analysis.preprocess(theblob)
        return process_blob.words

#testing class
web_search = websearch()
thewords = web_search.text_execution('blueberries.jpg')
urls = web_search.search_google(thewords)
for url in urls:
    print(url)
