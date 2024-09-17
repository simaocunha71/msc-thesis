import re
def find_adverb_position(sentence):
    adverb = re.findall(r'\b\w+ly\b', sentence)
    position = (sentence.index(adverb[0]), len(adverb[0]) + sentence.index(adverb[0]), adverb[0])
    return position