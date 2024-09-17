def first_non_repeating_character(s):
    char_dict = {}
    for c in s:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    for c in s:
        if char_dict[c] == 1:
            return c
    return None