from nltk.tokenize import word_tokenize
import re
def find_adverb_position(sentence):
    words = word_tokenize(sentence)
    adverbs = [word for word in words if re.match(r'^[a-z]+(ly)$', word)]
    if adverbs:
        return (words.index(adverbs[0]), len(''.join(words)) - len(adverbs[0]), adverbs[0])
    return None