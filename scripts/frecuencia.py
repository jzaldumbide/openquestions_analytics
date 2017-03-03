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




#from vaderSentiment.vaderSentiment import sentiment as vaderSentiment 
file=sys.argv[1]
print (file)

default_stopwords = set(nltk.corpus.stopwords.words('spanish'))
corpus = nltk.corpus.PlaintextCorpusReader('.', file)
with open(file,'r') as f:
    lines = f.read().split("\n")


print ("\n")
print("Numero de oraciones {}".format(len(lines)))
print ("Palabras totales=", len([word for sentence in corpus.sents() for word in sentence]))
print ("\n")
palabras=corpus.words()


palabras = [word for word in palabras if len(word) > 4]
contador=0
oracionrepetida="oracionrepetida"
temporal="temporal"
ingles="ingles"
sentiment="sentiment"
fdist = nltk.FreqDist(palabras)
print (fdist)

for word, frequency in fdist.most_common(15):
	print('La palabra <%s> se repite <%d> veces' % (word, frequency))
	#.encode('utf-8')
	#topword=word.encode('utf-8')
	topword=word
