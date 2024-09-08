def long_words(n,words):
    words = words.split(" ")
    long_words = [word for word in words if len(word) > n]
    return long_words