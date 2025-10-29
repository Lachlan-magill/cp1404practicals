"""
Word Occurrences
Estimate: 20 minutes
Actual:   28 minutes
"""

word_occurrences = {}
text = input("Text: ")


for word in text.split():
    frequency = word_occurrences.get(word, 0)
    word_occurrences[word] = frequency + 1


words = list(word_occurrences.keys())
words.sort()


max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_occurrences[word]}")