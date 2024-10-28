def first_non_repeating_character(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for c in s:
        if d[c] == 1:
            return c
    return None