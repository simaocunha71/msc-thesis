def next_Perfect_Square(num):
    """
    Given a positive integer num, find the next closest square number.
    """
    x = num.bit_length()
    y = 1 << x
    return y**2