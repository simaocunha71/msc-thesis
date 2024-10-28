def left_rotate(num, d):
    return (((num << d) % 0xFFFFFFFF) + (num >> (32 - d))) & 0xFFFFFFFF