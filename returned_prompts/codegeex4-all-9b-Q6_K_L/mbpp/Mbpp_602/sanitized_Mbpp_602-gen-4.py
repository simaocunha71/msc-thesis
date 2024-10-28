def first_repeated_char(s: str) -> str:
    char_dict = {}
    for char in s:
        if char in char_dict:
            return char
        char_dict[char] = True
    return None