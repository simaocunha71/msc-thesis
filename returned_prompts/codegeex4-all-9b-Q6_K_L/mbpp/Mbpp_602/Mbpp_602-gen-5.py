def first_repeated_char(s: str) -> str:
    chars = {}
    for char in s:
        if char in chars:
            return char
        else:
            chars[char] = 1
    return None

