def first_repeated_char(string):
    visited_chars = set()
    for char in string:
        if char in visited_chars:
            return char
        visited_chars.add(char)
    return None