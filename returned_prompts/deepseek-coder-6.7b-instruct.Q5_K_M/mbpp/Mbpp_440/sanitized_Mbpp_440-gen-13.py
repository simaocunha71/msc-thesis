import nltk
from nltk.corpus import wordnet
def find_adverb_position(sentence):
    text = nltk.word_tokenize(sentence)
    pos = nltk.pos_tag(text)
    for i in range(len(pos)):
        if pos[i][1] in ['RB', 'RBR', 'RBS']:
            return i, i+1, pos[i][0]