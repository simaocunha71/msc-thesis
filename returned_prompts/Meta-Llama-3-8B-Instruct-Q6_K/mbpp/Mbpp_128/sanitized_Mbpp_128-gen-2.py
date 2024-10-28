def long_words(n, sentence):
    words = sentence.split()
    return [word for word in words if len(word) > n]  # filter words with more than n characters