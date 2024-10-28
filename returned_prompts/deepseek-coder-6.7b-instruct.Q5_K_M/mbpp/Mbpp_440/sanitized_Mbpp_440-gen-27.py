import nltk
from nltk.corpus import wordnet
def find_adverb_position(sentence):
    text = nltk.word_tokenize(sentence)
    pos = nltk.pos_tag(text)
    for word in pos:
        if word[1] in ['RB', 'RBR', 'RBS']:
            return (text.index(word[0]), word[0])