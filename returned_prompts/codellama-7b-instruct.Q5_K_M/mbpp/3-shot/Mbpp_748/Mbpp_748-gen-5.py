
def capital_words_spaces(my_string):
    words = my_string.split()
    for i, word in enumerate(words):
        if word[0].isupper():
            words[i] = ' ' + word
    return ''.join(words)


