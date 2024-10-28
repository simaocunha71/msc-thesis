def first_non_repeating_character(s: str) -> str:
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    for c in s:
        if char_count[c] == 1:
            return c

    return None