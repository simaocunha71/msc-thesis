def find_char_long(text: str) -> list:
    words = text.split()
    long_words = [word for word in words if len(word) >= 4]
    return long_words