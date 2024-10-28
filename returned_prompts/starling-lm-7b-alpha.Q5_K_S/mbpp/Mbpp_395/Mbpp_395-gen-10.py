
def first_non_repeating_character(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c in s:
        if counts[c] == 1:
            return c
    return None


