
def count_upper(s):
    c = 0
    for i, ch in enumerate(s):
        if ch.isupper() and i % 2 == 0:
            c += 1
    return c
