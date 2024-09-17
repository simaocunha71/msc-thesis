from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk import pos_tag
import sys
def find_adverb_position(sentence):
    words = word_tokenize(sentence)
    tags = pos_tag(words)
    for i, word in enumerate(words):
        if wordnet.synsets(word) and tags[i][1] == 'RB':
            return i, words.index(word), word
    return None