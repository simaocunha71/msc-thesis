

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    result = ''
    while x > 0:
        rem = x % base  # remainder of division
        if not rem == 0:
            tmp = (rem // base)[::-1]
            result += tmp
            x -= rem * base
        else:
            break
    return result[::-1]
