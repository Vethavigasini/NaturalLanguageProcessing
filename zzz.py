def plural(word):
    if word.endswith(('s', 'x', 'z')):
        return word + "es"
    elif word.endswith('y'):
        return word[:-1] + "ies"
    else:
        return word + "s"

print(plural("cat"))
print(plural("box"))
print(plural("baby"))
