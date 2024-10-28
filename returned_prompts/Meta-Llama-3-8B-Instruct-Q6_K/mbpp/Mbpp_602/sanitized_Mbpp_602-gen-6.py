def first_repeated_char(s):
    seen = {}
    for char in s:
        if char in seen:
            return char
        seen[char] = True
    return None