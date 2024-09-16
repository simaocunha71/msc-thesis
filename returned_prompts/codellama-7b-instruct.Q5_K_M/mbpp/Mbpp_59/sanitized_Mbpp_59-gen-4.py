def is_octagonal(n):
    i = 1
    while i * (i + 1) / 2 <= n:
        i += 1
    return i * (i + 1) / 2