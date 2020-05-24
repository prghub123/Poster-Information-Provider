import os
import sys
import csv
from text_recognition import text_recog
from textblob import TextBlob
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
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
    #POS-tagging to extract useful words (maybe)
    full_string = ""
    for word in words:
        full_string += (word + ' ')
        #print(full_string)
        blob = TextBlob(full_string)
        return blob
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


#remove stopwords and potential URLs from text
def remove_noise(blob):
    #remove stopwords
    stop_words = set(stopwords.words('english'))
    stopwords_fil_blob = [element for element in blob.words if element not in stop_words]
    #remove URLs
    url_tags = ['.com', '.org', '.edu', '.gov', 'https', 'www.']
    for tag in url_tags:
        for element in stopwords_fil_blob:
            if tag in element:
                stopwords_fil_blob.remove(element)
    stopwords_fil_blob = ''.join(stopwords_fil_blob)
    return TextBlob(stopwords_fil_blob))

#lemmazation and stemming processing
def normalize(blob):
    lem = []
    singular_ blob = blob.words.singularize() #singularize the words; helps with generalizing search
    #extract each word in the new blob
    for word in singular_blob.words:
        #convert to Word object
        w = Word(word)
        #invoke lemmatize method and append to list
        lem.append(w.lemmatize())
    lem = ''.join(lem)
    return TextBlob(lem)

#process text blob to remove excess information
#utilizes two helper functions to remove noise and normalize
def preprocess(blob):
     new_blob = remove_noise(blob)
     processed_blob = normalize(new_blob)
     return processed_blob
