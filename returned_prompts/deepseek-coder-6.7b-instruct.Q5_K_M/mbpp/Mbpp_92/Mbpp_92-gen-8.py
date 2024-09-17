
def is_undulating(n):
    s = str(n)
    return all(a != b for a, b in zip(s, s[1:]))


