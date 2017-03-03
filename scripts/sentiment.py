#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import cess_esp as cess
from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text
from string import punctuation
from collections import Counter
from nltk.corpus import stopwords
import string
import sys
import codecs
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

file=sys.argv[1]

default_stopwords = set(nltk.corpus.stopwords.words('english'))
corpus = nltk.corpus.PlaintextCorpusReader('.', file)

analyzer = SentimentIntensityAnalyzer()

with open(file,'r') as f:
    lines = f.read().split("\n")
    
for i,line in enumerate(lines):
	
	oracionrepetida=line
	temporal='hola'
	temporal=TextBlob(oracionrepetida)
	sentiment=TextBlob(str(temporal))
	vs=analyzer.polarity_scores(oracionrepetida)
	#print(oracionrepetida)
	print(str(sentiment.sentiment.polarity)+"<>"+str(vs['compound']))
	