def capital_words_spaces(s):
    words = s.split()
    for i, word in enumerate(words):
        if word[0].isupper():
            words[i] = ' ' + word
    return ''.join(words)
