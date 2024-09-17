
import nltk
from nltk.corpus import wordnet
def find_adverb_position(sentence):
  text = nltk.word_tokenize(sentence)
  pos_tags = nltk.pos_tag(text)
  for i in range(len(pos_tags)):
    if pos_tags[i][1] in ['RB', 'RBR', 'RBS', 'WRB']:
      return i, i+1, pos_tags[i][0]


