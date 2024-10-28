def number_ctr(s):
    for c in s:
        if c.isdigit():
            return 1
    return 0