import re
from collections import namedtuple
AdverbPosition = namedtuple('AdverbPosition', ['start', 'end', 'adverb'])
def find_adverb_position(sentence):
    adverbs = ['clearly', 'quickly', 'loudly', 'slowly', 'silently', 'quietly']
    for adverb in adverbs:
        match = re.search(r'\b' + re.escape(adverb) + r'\b', sentence)
        if match:
            return AdverbPosition(start=match.start(), end=match.end(), adverb=adverb)
    return None