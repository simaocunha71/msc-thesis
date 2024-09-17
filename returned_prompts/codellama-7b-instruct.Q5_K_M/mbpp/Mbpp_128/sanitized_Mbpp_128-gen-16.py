def long_words(n: int, words: str) -> list:
    return [word for word in words.split() if len(word) > n]