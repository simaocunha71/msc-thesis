def first_repeated_char(string):
    seen_chars = set()
    for char in string:
        if char in seen_chars:
            return char
        seen_chars.add(char)
    return None