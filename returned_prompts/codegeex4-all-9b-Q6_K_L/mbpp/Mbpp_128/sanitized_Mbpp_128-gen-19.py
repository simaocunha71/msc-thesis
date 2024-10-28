def long_words(n: int, words: str) -> list:
    words_list = words.split()
    long_words = [word for word in words_list if len(word) > n]
    return long_words