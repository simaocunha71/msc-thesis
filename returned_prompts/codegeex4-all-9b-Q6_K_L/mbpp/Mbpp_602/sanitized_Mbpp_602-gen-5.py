def first_repeated_char(s: str) -> str:
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None