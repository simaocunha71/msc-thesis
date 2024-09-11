"""
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn

def find_adverb_position(sentence):
    tokens = word_tokenize(sentence)
    for i, token in enumerate(tokens):
        if wn.synsets(token)[0].pos() == 'ADV':
            return (i, tokens[i], tokens[i+1:])

find_adverb_position("clearly!! we can see the sky") #(0, 'clearly', ['we', 'can', 'see', 'the', 'sky'])

"""

from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn

def find_adverb_position(sentence):
    tokens = word_tokenize(sentence)
    for i, token in enumerate(tokens):
        if wn.synsets(token)[0].pos() == 'ADV':
            return (i, tokens[i], tokens[i+1:])

find_adverb_position("clearly!! we can see the sky") #(0, 'clearly', ['we', 'can', 'see', 'the', 'sky'])




# 上記の方法で、アドバーブが複数ある場合、最初のアドバーブのみを返してしまいます。
# 例えば、「昨日、私は暑いです。」を処理した場合、最初のアドバーブ（昨日）が返されます。
# したがって、以下の方法で、すべてのアドバーブを返します。


def find_adverb_position(sentence):
    tokens = word_tokenize(sentence)
    adverbs = []
    for token in tokens:
        if wn.synsets(token)[0].pos() == 'ADV':
            adverbs.append(token)
    return adverbs

find_adverb_position("昨日、私は暑