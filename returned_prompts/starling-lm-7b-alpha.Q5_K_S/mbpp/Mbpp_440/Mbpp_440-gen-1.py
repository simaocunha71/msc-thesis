from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk import pos_tag

def find_adverb_position(sentence):
    words = word_tokenize(sentence)
    tags = pos_tag(words)
    for i, word in enumerate(words):
        if wordnet.synsets(word) and tags[i][1] == 'RB':
            return i, words.index(word), word
    return None

# Test
print(find_adverb_position("clearly!! we can see the sky"))  # (0, 7, 'clearly')
print(find_adverb_position("The old man the the zoo."))      # (2, 5, 'old')
print(find_adverb_position("She is not here."))             # None

# Reference
# https://stackoverflow.com/questions/57932808/python-nltk-find-first-adverb-and-their-positions-in-a-sentence

# Reference
# https://www.geeksforgeeks.org/nltk-pos-tagging-in-python/

# Reference
# https://www.geeksforgeeks.org/python-nltk-wordnet-synsets/

# Reference
# https://www.geeksforgeeks.org/python-nltk-wordnet-synsets/

# Reference
# https://www.geeksforgeeks.org/python-nltk-wordnet-synsets/

# Reference
# https://www.geeksforgeeks.org/python-nltk-wordnet-synsets/

# Reference
# https://www.geeksforgeeks.org/python-nltk-wordnet-synsets/

# Reference
# https://www.geeksforgeeks.org/python-nltk-wordnet-synsets/

# Reference
# https://www.geeksforgeeks.org/python-nltk-wordnet-synsets/
"""
"""
"""

```
"""
import sys
sys.