def first_non_repeating_character(s: str) -> str:
    for c in s:
        if s.count(c) == 1:
            return c
    return None

