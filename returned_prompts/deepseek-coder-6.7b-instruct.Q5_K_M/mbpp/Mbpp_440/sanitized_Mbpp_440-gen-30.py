import nltk
def find_adverb_position(s):
    text = nltk.word_tokenize(s)
    pos_tagged = nltk.pos_tag(text)
    for i in range(len(pos_tagged)):
        if pos_tagged[i][1] == 'RB':
            return i, i+1, pos_tagged[i][0]