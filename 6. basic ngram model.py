import random

text = "I love python and I love coding in python"
words = text.split()

bigrams = {}
for i in range(len(words) - 1):
    key = words[i]
    value = words[i + 1]
    if key not in bigrams:
        bigrams[key] = []
    bigrams[key].append(value)

current = "I"
result = [current]

for _ in range(5):
    if current in bigrams:
        next_word = random.choice(bigrams[current])
        result.append(next_word)
        current = next_word
    else:
        break

print("Generated Text:", " ".join(result))
