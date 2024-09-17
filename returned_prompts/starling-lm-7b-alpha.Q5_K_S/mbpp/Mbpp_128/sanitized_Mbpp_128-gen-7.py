def long_words(n,words):
    return [i for i in words.split() if len(i)>n]