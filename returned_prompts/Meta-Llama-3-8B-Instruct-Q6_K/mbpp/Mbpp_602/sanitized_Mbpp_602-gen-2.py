def first_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return char
        char_count[char] = 1
    return None