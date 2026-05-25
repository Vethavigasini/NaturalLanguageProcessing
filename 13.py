import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "Cats are running in the garden"

tokens = word_tokenize(text)
tags = pos_tag(tokens)

print(tags)
