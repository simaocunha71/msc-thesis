def is_nonagonal(n):
    x = 2**(n-1)
    return x * (x + 1) * (2 * x + 1) // 6