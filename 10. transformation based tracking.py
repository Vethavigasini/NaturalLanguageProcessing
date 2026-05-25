words = ["Dogs", "bark", "loudly"]

tags = [("Dogs", "NN"), ("bark", "NN"), ("loudly", "RB")]

new_tags = []
for word, tag in tags:
    if word.endswith("s") and tag == "NN":
        tag = "NNS"
    new_tags.append((word, tag))

print(new_tags)
