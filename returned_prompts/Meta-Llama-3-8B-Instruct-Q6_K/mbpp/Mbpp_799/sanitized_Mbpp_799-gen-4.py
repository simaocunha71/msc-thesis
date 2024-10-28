def left_rotate(n, d):
    d = d % 32
    mask = (1 << d) - 1
    return ((n << d) | (n >> (32 - d))) & ~mask