def number_ctr(s: str) -> int:
    count = 0
    for c in s:
        if c.isdigit():
            count += 1
    return count