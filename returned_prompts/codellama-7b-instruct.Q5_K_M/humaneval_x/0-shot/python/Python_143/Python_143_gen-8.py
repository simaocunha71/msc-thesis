
from math import sqrt

def words_in_sentence(sentence):
    words = sentence.split(" ")
    for word in words:
        if int(sqrt(len(word))) ** 2 != len(word):
            words.remove(word)
    return " ".join(words)
