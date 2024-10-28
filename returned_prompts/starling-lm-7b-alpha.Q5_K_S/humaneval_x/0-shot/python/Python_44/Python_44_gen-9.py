

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
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


# Here are some tests for your function:
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'


# More tests:
print(change_base(10, 4))  # '22'
print(change_base(100, 3))  # '102'
print(change_base(100, 2))  # '1100100'


# And some edge cases:
print(change_base(0, 2))  # '0'
print(change_base(1, 2))  # '1'
print(change_base(10, 10))  # '10'


# And some errors:
try:
    print(change_base(0, 0))  # Should raise ValueError: base should not be 0
except ValueError as e:
    print(e)
try:
    print(change_base('abc', 2))  # Should raise ValueError: x should be int
except ValueError as e:
    print(e)


# And some stress test:
print(change_base(2 ** 30, 2))  # '1111111111111111111111111111110'















