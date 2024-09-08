def first_non_repeating_character(s: str) -> str:
    seen = {}
    for c in s:
        if c in seen:
            seen[c] += 1
        else:
            seen[c] = 1
    for c in s:
        if seen[c] == 1:
            return c
    return None