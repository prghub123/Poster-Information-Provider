import os
import sys
import csv
from text_recognition import text_recog
from textblob import TextBlob
from textblob import Word
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import boto3


#creates class to analyze text: sentiment, lemmazation, filtering, etc
#returns text
class text_analysis():
    #function to replace contractions with expanded words; utilizes dictionary of possible contractions
    #returns list of all elements without contructions
    def remove_contractions(self, text):
        contractions = {
        "ain't": "am not / are not",
        "aren't": "are not / am not",
        "can't": "cannot",
        "can't've": "cannot have",
        "'cause": "because",
        "could've": "could have",
        "couldn't": "could not",
        "couldn't've": "could not have",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hadn't've": "had not have",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he had / he would",
        "he'd've": "he would have",
        "he'll": "he shall / he will",
        "he'll've": "he shall have / he will have",
        "he's": "he has / he is",
        "how'd": "how did",
        "how'd'y": "how do you",
        "how'll": "how will",
        "how's": "how has / how is",
        "i'd": "I had / I would",
        "i'd've": "I would have",
        "i'll": "I shall / I will",
        "i'll've": "I shall have / I will have",
        "i'm": "I am",
        "i've": "I have",
        "isn't": "is not",
        "it'd": "it had / it would",
        "it'd've": "it would have",
        "it'll": "it shall / it will",
        "it'll've": "it shall have / it will have",
        "it's": "it has / it is",
        "let's": "let us",
        "ma'am": "madam",
        "mayn't": "may not",
        "might've": "might have",
        "mightn't": "might not",
        "mightn't've": "might not have",
        "must've": "must have",
        "mustn't": "must not",
        "mustn't've": "must not have",
        "needn't": "need not",
        "needn't've": "need not have",
        "o'clock": "of the clock",
        "oughtn't": "ought not",
        "oughtn't've": "ought not have",
        "shan't": "shall not",
        "sha'n't": "shall not",
        "shan't've": "shall not have",
        "she'd": "she had / she would",
        "she'd've": "she would have",
        "she'll": "she shall / she will",
        "she'll've": "she shall have / she will have",
        "she's": "she has / she is",
        "should've": "should have",
        "shouldn't": "should not",
        "shouldn't've": "should not have",
        "so've": "so have",
        "so's": "so as / so is",
        "that'd": "that would / that had",
        "that'd've": "that would have",
        "that's": "that has / that is",
        "there'd": "there had / there would",
        "there'd've": "there would have",
        "there's": "there has / there is",
        "they'd": "they had / they would",
        "they'd've": "they would have",
        "they'll": "they shall / they will",
        "they'll've": "they shall have / they will have",
        "they're": "they are",
        "they've": "they have",
        "to've": "to have",
        "wasn't": "was not",
        "we'd": "we had / we would",
        "we'd've": "we would have",
        "we'll": "we will",
        "we'll've": "we will have",
        "we're": "we are",
        "we've": "we have",
        "weren't": "were not",
        "what'll": "what shall / what will",
        "what'll've": "what shall have / what will have",
        "what're": "what are",
        "what's": "what has / what is",
        "what've": "what have",
        "when's": "when has / when is",
        "when've": "when have",
        "where'd": "where did",
        "where's": "where has / where is",
        "where've": "where have",
        "who'll": "who shall / who will",
        "who'll've": "who shall have / who will have",
        "who's": "who has / who is",
        "who've": "who have",
        "why's": "why has / why is",
        "why've": "why have",
        "will've": "will have",
        "won't": "will not",
        "won't've": "will not have",
        "would've": "would have",
        "wouldn't": "would not",
        "wouldn't've": "would not have",
        "y'all": "you all",
        "y'all'd": "you all would",
        "y'all'd've": "you all would have",
        "y'all're": "you all are",
        "y'all've": "you all have",
        "you'd": "you had / you would",
        "you'd've": "you would have",
        "you'll": "you shall / you will",
        "you'll've": "you shall have / you will have",
        "you're": "you are",
        "you've": "you have"
        }
        #iterate through words in text and determine if contractions exist
        for index in range(0, len(text)):
            #if the token is a contraction, replace the contractionwith the corresponding expanded word(key -> value) in dictionary
            #print(text[index])
            #print("Lowercase word")
            #print(text[index].lower())
            if(text[index].lower() in contractions):
                text[index] = contractions[text[index].lower()]
        return text
    #invokes AWS text recognition from image parameter
    def recognize_text(self, picture):
        test = text_recog();
        test.open_img(picture)
        text = test.extract_text()
        return text

    #filter out individual words
    #returns Textblob object
    def filter_words(self, text):
        text[:] = [x for x in text if not ('LINE' == x.get('Type'))]
        #print("Filtering out Lines")
        #print(text)
        #print(text)
        #filter words based on confidence level
        words = [x.get('DetectedText') for x in text if (x.get('Confidence') > 50)]
        #print("Filtering out from confidence level")
        #print(words)
        #replace potential contractions
        new_words = self.remove_contractions(words)
        #print(words)
        full_string = ""
        for word in new_words:
            full_string += (word + ' ')
        #print("Here is the full string ")
        #print(full_string)
        blob = TextBlob(full_string)
        return blob
        #print(tags)
        #print(nouns)

    #function to assess sentiment of text
    #returns textblob object
    def sentiment(self, blob):
        #print("Passed in Sentiment blob")
        #print(blob.words)
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
    #returns textblob object
    def remove_noise(self, blob):
        #remove stopwords
        stop_words = set(stopwords.words('english'))
        stopwords_fil_blob = [element for element in blob.words if element.lower() not in stop_words]
        #remove URLs
        url_tags = ['.com', '.org', '.edu', '.gov', 'https', 'www.']
        #iterate through tags
        for tag in url_tags:
            #iterate through words
            for element in stopwords_fil_blob:
                #if element has any of the tags, remove the element
                if tag in element:
                    stopwords_fil_blob.remove(element)
        #convert curated words to strings
        stopwords_fil_blob = [str(element) for element in stopwords_fil_blob]
        stopwords_fil_blob = ' '.join(stopwords_fil_blob)
        return TextBlob(stopwords_fil_blob)

    #lemmazation and stemming processing
    #returns textblob
    def normalize(self, blob):
        lem = []
        singular_blob = blob.words.singularize() #singularize the words; helps with generalizing search
        #extract each word in the new blob
        for word in singular_blob:
            #convert to Word object
            w = Word(word)
            #invoke lemmatize method and append to list
            lem.append(w.lemmatize())
        lem = [str(element) for element in lem]
        lem = ' '.join(lem)
        return TextBlob(lem)

    #process text blob to remove excess information
    #utilizes two helper functions to remove noise and normalize
    #returns textblob object
    def preprocess(self, blob):
         new_blob = self.remove_noise(blob)
         #print(new_blob.words)
         processed_blob = self.normalize(new_blob)
         return processed_blob



#testing class
