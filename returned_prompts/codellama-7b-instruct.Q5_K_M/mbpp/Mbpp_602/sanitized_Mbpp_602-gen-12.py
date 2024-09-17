def first_repeated_char(s: str) -> str:
    for c in s:
        if s.count(c) > 1:
            return c
    return None