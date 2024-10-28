def first_repeated_char(s):
    for c in s:
        if s.count(c) > 1:
            return c
    return None
