 ka# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:55:40 2019

@author: batra
"""


import pandas as pd
import nltk
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from collections import Counter
from gensim.corpora.dictionary import Dictionary
from gensim.models.tfidfmodel import TfidfModel
import string
import re
from textblob import TextBlob 


#sample_df = pd.read_csv('Input/twitter1.csv')
#sample_df.head()
#MKC_raw_data = sample_df.iloc[0,3]

def remove_punctuation(text):
    no_punct = "".join([c for c in text if c not in string.punctuation])
    return no_punct

def remove_links(text):
    clean_tweet = re.sub(r'http\*',"",text)
    return clean_tweet

def remove_stopwords(text):
    words = [w for w in text if w not in stopwords.words('english')]
    return words

lemmatizer = WordNetLemmatizer()
def word_lemmatizer(text):
    lem_text = [lemmatizer.lemmatize(i) for i in text]
    return lem_text

def word_tokenizer(text):
    tokenized = set(word_tokenize(text))
    return tokenized

def removeAlphaNumericWords(text):
    return re.sub("\S*\d\S*", "", text).strip()
    
def removeSpecialChars(text):
    return re.sub('[^a-zA-Z]', ' ', text)
    
def remove_tickers(text):
    return re.sub(r'\$\s\w*',"",text)

def TextCleaning(text):
    text = remove_tickers(text)
    text = remove_links(text)
    text = removeAlphaNumericWords(text)
    text = removeSpecialChars(text) 
    # Lower casing
    text = text.lower()  
    #Tokenization
    text = word_tokenizer(text)
    #Removing Stopwords and Lemmatization
    text = remove_stopwords(text)
    
    return text


# after creating list of cleaned texts
def create_BoW(texts):
    tokenized_corpus = [TextCleaning(text) for text in texts]
    d = Dictionary(tokenized_corpus)
    d.token2id
    return d

def create_tfidf(texts):
    tokenized_corpus = [TextCleaning(text) for text in texts]
    d = Dictionary(tokenized_corpus)
    bowcorpus = [d.doc2bow(doc) for doc in tokenized_corpus]
    tfidf = TfidfModel(bowcorpus)
    return tfidf


Corpus = pd.read_csv('Output/Corpus.csv')
Corpus['CleanText']=""
for i in Corpus.index:
    Corpus['CleanText'][i] = TextCleaning(Corpus['Text'][i])
    Jointext = ""
    for j in Corpus['CleanText'][i]:
        Jointext += " " + j
    Corpus['CleanText'][i] = Jointext

Corpus['Sentiment'] = ""
for i in Corpus.index:
    Corpus['Sentiment'][i] = TextBlob(Corpus['CleanText'][i]).sentiment.polarity
    
# Need to finalize the total scoring method.
# Could possibly include the upvote ratio and the number of comments.
Corpus['TotScore'] = ""
for i in Corpus.index:
    Corpus['TotScore'][i] = Corpus['score'][i]*Corpus['Sentiment'][i]

Sentiments = Corpus[['INDEX', 'TotScore']]
Sentiments['TotScore'] = Sentiments['TotScore'].astype(float)
Sentiments = Sentiments.groupby('INDEX').mean()
Sentiments.to_csv('Output/Sentiments7.csv')