def find_char_long(s: str) -> set:
    words = s.split()
    return set([word for word in words if len(word) >= 4])