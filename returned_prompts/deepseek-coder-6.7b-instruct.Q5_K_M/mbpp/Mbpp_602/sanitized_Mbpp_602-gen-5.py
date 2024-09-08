def first_repeated_char(s: str):
    chars = set()
    for char in s:
        if char in chars:
            return char
        chars.add(char)
    return None