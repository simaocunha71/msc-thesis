

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    gcd = 0
    while a != b:
        m = int((a // b)) - 1
        if gcd < m:
            gcd += m
        else:
            return gcd
