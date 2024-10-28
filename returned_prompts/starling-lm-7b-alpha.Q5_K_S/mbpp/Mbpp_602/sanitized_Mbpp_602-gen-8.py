def first_repeated_char(s):
    char_set = set()
    for c in s:
        if c in char_set:
            return c
        else:
            char_set.add(c)
    return None