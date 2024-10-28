
import nltk
from nltk.corpus import stopwords
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
def find_adverb_position(sent):
  words = nltk.word_tokenize(sent)
  pos_tags = nltk.pos_tag(words)
  for i, (word, tag) in enumerate(pos_tags):
    if tag in ['RBR', 'RBS'] and word not in stop_words:
      return i, i+1, word


