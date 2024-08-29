def long_words(n,words):
    result = [word for word in words.split() if len(word) > n]
    return result