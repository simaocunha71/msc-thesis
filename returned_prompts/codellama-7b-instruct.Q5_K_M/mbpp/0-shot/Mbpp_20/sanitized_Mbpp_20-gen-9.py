def is_woodall(n):
    s = str(n)
    return all(s.count(d) == 2 for d in '13579')