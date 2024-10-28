def long_words(n, string):
    return [word for word in string.split() if len(word) > n]