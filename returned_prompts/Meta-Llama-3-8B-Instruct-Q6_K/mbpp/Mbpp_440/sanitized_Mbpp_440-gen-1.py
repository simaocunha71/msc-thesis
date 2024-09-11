import re
def find_adverb_position(sentence):
    adverbs = re.findall(r'\b(ly)\b', sentence)
    for i, word in enumerate(sentence.split()):
        if word in adverbs:
            return i, i + len(word), word
    return -1, -1, ''