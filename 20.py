import nltk

# Run this ONLY FIRST TIME
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "The boy is playing cricket"
words = word_tokenize(text)
tags = pos_tag(words)

print(tags)
