from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
def find_adverb_position(sentence):
    token_list = word_tokenize(sentence)
    tagged_list = pos_tag(token_list)
    for i in range(len(tagged_list)):
        if tagged_list[i][1] == "RB":
            return (i, tagged_list[i][0], tagged_list[i][0])