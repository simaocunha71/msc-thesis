def capital_words_spaces(s: str) -> str:
    return ' '.join([word for word in s.split() if word[0].isupper()])