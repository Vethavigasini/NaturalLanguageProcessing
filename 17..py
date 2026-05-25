import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet

syn = wordnet.synsets("bank")

for s in syn[:3]:
    print(s.definition())
