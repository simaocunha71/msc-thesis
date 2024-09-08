def first_non_repeating_character(s):
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    for c in s:
        if count[c] == 1:
            return c
    return None