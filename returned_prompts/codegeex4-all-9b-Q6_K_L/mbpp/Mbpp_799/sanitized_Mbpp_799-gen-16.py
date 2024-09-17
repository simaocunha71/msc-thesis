def left_rotate(num, d):
    return (num << d) | (num >> (32 - d))