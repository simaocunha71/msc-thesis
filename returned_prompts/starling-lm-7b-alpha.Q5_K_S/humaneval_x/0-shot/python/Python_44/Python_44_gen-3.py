

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

    if x < 0:
        return '-' + change_base(-x, base)
    if x == 0:
        return '0'

    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    digits.reverse()

    return ''.join(digits)

# Here is some test cases for the function
print(change_base(8, 3))
print(change_base(8, 2))
print(change_base(7, 2))

















# Here is some test cases for the function
print(change_base(8, 3))
print(change_base(8, 2))
print(change_base(7, 2))















































































































































































































