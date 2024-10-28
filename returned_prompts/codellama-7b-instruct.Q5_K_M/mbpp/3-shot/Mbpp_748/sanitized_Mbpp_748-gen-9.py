def capital_words_spaces(s: str) -> str:
    words = s.split()
    return ' '.join([word for word in words])