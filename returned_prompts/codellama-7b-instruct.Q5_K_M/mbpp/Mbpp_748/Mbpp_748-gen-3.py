def capital_words_spaces(s):
    words = s.split()
    return ' '.join(w.title() for w in words)


