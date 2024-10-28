def cycpattern_check(a , b):
    b_len = len(b)
    b_rotations = [b[i:] + b[:i] for i in range(b_len)]
    return any(rotation in a for rotation in b_rotations)