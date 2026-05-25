import re

words = ["running", "beautiful", "cats", "eat"]
tagged = []

for word in words:
    if re.search(r'ing$', word):
        tag = "VBG"
    elif re.search(r'ful$', word):
        tag = "JJ"
    elif re.search(r's$', word):
        tag = "NNS"
    else:
        tag = "NN"
    tagged.append((word, tag))

print(tagged)
