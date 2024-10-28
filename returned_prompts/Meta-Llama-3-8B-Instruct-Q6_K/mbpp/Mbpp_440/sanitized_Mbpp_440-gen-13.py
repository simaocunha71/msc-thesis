import re
def find_adverb_position(sentence):
    adverbs = ['quickly', 'slowly', 'loudly', 'softly', 'silently', 'clearly', 'quietly', 'noisily', 'gently', 'roughly', 'smoothly']
    for adverb in adverbs:
        if re.search(adverb, sentence):
            return re.search(adverb, sentence).start(), re.search(adverb, sentence).end(), adverb
    return -1, -1, ''