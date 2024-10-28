def number_ctr(s: str) -> int:
    ctr = 0
    for i in s:
        if i.isdigit():
            ctr += 1
    return ctr