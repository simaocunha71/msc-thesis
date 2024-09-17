
def long_words(n, words: str):
    return [word for word in words.split() if len(word) > n]


