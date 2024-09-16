def left_rotate(a, d):
    mask = 0xffffffff
    return (a << d) | (a & mask >> (32 - d))

