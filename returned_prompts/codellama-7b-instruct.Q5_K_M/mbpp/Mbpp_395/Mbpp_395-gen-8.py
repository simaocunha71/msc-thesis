
def first_non_repeating_character(s):
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
        else:
            seen.remove(char)
    if len(seen) == 0:
        return None
    else:
        return seen.pop()


