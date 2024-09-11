from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag

def find_adverb_position(sentence):
    token_list = word_tokenize(sentence)
    tagged_list = pos_tag(token_list)
    for i in range(len(tagged_list)):
        if tagged_list[i][1] == "RB":
            return (i, tagged_list[i][0], tagged_list[i][0])


#assert find_adverb_position("clearly!! we can see the sky")==(0, 'clearly', 'clearly')
#print(find_adverb_position("clearly!! we can see the sky"))

"""
def find_adverb_position(sentence):
    tagger = nltk.pos_tag([sentence])
    for tag in tagger:
        if tag[1] == 'RB' or tag[1] == 'RBR' or tag[1] == 'RBS':
            return tag[0], tag[1], tag[0]
    return None
#assert find_adverb_position("clearly!! we can see the sky")==(0, 'clearly', 'clearly')
#print(find_adverb_position("clearly!! we can see the sky"))
"""

"""
def find_adverb_position(sentence):
    tagger = nltk.pos_tag(nltk.word_tokenize(sentence))
    for tag in tagger:
        if tag[1] == 'RB' or tag[1] == 'RBR' or tag[1] == 'RBS':
            return tag[0], tag[1], tag[0]
    return None
#assert find_adverb_position("clearly!! we can see the sky")==(0, 'clearly', 'clearly')
#print(find_adverb_position("clearly!! we can see the sky"))
"""

"""
def find_adverb_position(sentence):
    for i in range(len(sentence)):
        if sentence[i] in ['clearly', 'quickly