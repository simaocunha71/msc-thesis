def is_octagonal(n):
    n = int(n)
    if n < 1:
        return False
    a = (1 + 2 * (1 + 2 * (1 + 2 * (1 + 2 * (1 + 2 * (1 + 2 * (1 + 2 * (n - 1))))))))
    return n == a