
def capital_words_spaces(sentence):
    sentence_list = sentence.split()
    new_sentence = ''
    for word in sentence_list:
        if word[0].isupper():
            new_sentence += word + ' '
        else:
            new_sentence += word
    return new_sentence[:-1]


