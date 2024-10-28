def is_octagonal(n):
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return False
    oct = 1 + 9 * ((n - 1) // 2) ** 2
    return oct % (2 * (n + 1)) == 0 and oct % (2 * n) == 0