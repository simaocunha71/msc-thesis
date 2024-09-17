
import nltk
from nltk.corpus import brown
nltk.download('brown')
nltk.download('averaged_perceptron_tagger')

def find_adverb_position(sent):
  text = nltk.word_tokenize(sent)
  pos_tags = nltk.pos_tag(text)
  for i in range(len(pos_tags)):
    if pos_tags[i][1] == 'RB':
      return (i, i+1, pos_tags[i][0])


