def first_repeated_char(s: str) -> str:
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)
    return None

