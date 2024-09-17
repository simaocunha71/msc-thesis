
def capital_words_spaces(word):
    if word[0].isupper():
        return word.replace(' ', '') + ' '
    else:
        return word


