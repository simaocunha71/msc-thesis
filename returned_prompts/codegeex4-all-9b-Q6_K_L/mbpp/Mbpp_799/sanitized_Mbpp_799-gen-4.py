def left_rotate(n, d):
    """
    Rotate left bits by d bits a given number.
    """
    return (n << d) | (n >> (32 - d))