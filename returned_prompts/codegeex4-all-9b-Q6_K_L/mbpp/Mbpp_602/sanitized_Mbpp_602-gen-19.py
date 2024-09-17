def first_repeated_char(s: str) -> str:
    char_counts = {}
    for char in s:
        if char in char_counts:
            return char
        char_counts[char] = 1
    return None