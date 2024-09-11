def is_woodall(n):
    s = 0
    k = n
    while k > 0:
        s += k % 10
        k //= 10
    return s ** 2 == n * (s + 1) * (2 * s + 1) - 1