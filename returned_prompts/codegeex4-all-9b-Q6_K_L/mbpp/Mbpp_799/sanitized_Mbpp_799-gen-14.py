def left_rotate(n, d):
    n, d = n & 0xFFFFFFFF, d & 31
    return ((n << d) | (n >> (32 - d))) & 0xFFFFFFFF