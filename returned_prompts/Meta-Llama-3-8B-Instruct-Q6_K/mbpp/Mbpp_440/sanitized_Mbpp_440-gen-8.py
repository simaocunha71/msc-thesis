import re
def find_adverb_position(sentence):
    adverbs = re.findall(r'\b(adv|ly)\b', sentence)
    if adverbs:
        return (0, sentence.index(adverbs[0][0]), adverbs[0][0])
    else:
        return None