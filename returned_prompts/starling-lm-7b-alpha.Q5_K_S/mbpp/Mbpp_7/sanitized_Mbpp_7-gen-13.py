def find_char_long(sentence: str) -> set:
    return set(word for word in sentence.split() if len(word) >= 4)