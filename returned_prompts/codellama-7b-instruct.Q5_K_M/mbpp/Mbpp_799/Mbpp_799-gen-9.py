
def left_rotate(num: int, d: int) -> int:
    mask = 0xffffffff
    d %= 32
    return ((num << d) & mask) | (num >> (32 - d))


