import os
import sys
import csv
from text_recognition import text_recog
from textblob import TextBlob
import boto3

def recognize_text(picture):
    test = text_recog();
    test.open_img(picture)
    text = test.extract_text()
    return text

#filter out individual words
def filter_words(text):
    text[:] = [x for x in text if not ('LINE' == x.get('Type'))]
    #print(text)
    #filter words based on confidence level
    words = [x.get('DetectedText') for x in text if (x.get('Confidence') > 50)]
    #print(words)
    #POS-tagging to extract useful words
    full_string = ""
    for word in words:
        full_string += (word + ' ')
        #print(full_string)
        blob = TextBlob(full_string)
        tags = blob.tags #list of tuples (assigning POS tag to each word in string)
        nouns = blob.noun_phrases #WordList of nouns present in string
        #print(tags)
        #print(nouns)

#function to assess sentiment of text
def sentiment(blob):
    subject = blob.sentiment.subjectivity
    polar = blob.sentiment.polarity
    print("Subjectivity Rating: ", subject)
    print("Polarity Rating: ", polar)
    #assess subjectivity
    if(subject < 0.1):
        print("Source appears to be very objective")
    if(subject > 0.1 and subject < 0.5):
        print("Source appears to be fairly objective")
    if(subject > 0.5 and subject < 0.9):
        print("Source appears to be fairly subjective")
    if(subject > 0.9):
        print("Source appears to be very subjective")
