def left_rotate(num, d):
    mask = 0xffffffff
    return ((num << d) & mask) | (num >> (32-d))