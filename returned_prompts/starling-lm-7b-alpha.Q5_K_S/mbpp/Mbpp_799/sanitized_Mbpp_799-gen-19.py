def left_rotate(num: int, d: int):
    return (num << d) | (num >> (32 - d))