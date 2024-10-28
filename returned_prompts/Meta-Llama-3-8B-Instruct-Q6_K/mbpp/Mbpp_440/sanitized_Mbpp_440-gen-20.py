import nltk
from nltk import pos_tag
def find_adverb_position(sentence):
    words = sentence.split()
    tagged = pos_tag(words)
    for i, (word, pos) in enumerate(tagged):
        if pos.startswith('RB'):  # RB is the tag for adverbs
            return i, i+len(word), word
    return None