from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
def find_adverb_position(sentence):
    tokens = word_tokenize(sentence)
    for i, token in enumerate(tokens):
        if wn.synsets(token)[0].pos() == 'ADV':
            return (i, tokens[i], tokens[i+1:])