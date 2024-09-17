
def long_words(n: int, text: str) -> list:
    return [word for word in text.split() if len(word) > n]


