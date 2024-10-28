
import nltk
from nltk.corpus import stopwords
def find_adverb_position(sentence):
  words = nltk.word_tokenize(sentence)
  pos_tags = nltk.pos_tag(words)
  for i in range(len(pos_tags)):
    if pos_tags[i][1] == 'RB':
      return i, i+1, pos_tags[i][0]
  return None


