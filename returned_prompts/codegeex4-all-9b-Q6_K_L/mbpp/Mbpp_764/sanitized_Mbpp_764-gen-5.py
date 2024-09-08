def number_ctr(s: str) -> int:
    ctr = 0
    for c in s:
        if c.isdigit():
            ctr += 1
    return ctr