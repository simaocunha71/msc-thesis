def first_non_repeating_character(s):
    for index, char in enumerate(s):
        if s.count(char) == 1:
            return char
    return None