import re
import string
def find_adverb_position(sentence):
    adverbs = ['quickly', 'loudly', 'clearly', 'brightly', 'slowly', 'silently', 'quietly', 'gently', 'bravely', 'boldly']
    adverb = None
    position = None
    for i, word in enumerate(re.split(r'\W+', sentence)):
        if word.lower() in [a.lower() for a in adverbs]:
            adverb = word
            position = i
            break
    return position, position + len(adverb), adverb