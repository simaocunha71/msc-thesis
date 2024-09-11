def left_rotate(n, d):
    return (n << d) | (n >> (32 - d))  # 32 is the number of bits in a 32-bit integer