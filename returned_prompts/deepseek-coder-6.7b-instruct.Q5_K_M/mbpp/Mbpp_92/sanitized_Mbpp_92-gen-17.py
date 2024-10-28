def is_undulating(n):
    n = str(n)
    return all(a != b for a, b in zip(n, n[1:]))