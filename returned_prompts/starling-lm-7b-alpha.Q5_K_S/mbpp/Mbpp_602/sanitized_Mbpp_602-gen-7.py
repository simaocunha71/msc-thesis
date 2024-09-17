def first_repeated_char(s):
    seen_chars = set()
    for c in s:
        if c in seen_chars:
            return c
        seen_chars.add(c)
    return None