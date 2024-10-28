def first_repeated_char(s):
    for index, char in enumerate(s):
        if s.count(char) > 1:
            return char
    return None