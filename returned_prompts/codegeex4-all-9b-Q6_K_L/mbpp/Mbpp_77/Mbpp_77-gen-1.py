def is_Diff(n):
    n = str(n)
    if len(n) % 2 == 0:
        return n[::2] == n[1::2]
    else:
        return n[0] == n[1:]