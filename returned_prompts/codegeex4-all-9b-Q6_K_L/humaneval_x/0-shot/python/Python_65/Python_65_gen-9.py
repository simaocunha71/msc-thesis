def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[-shift:] + s[:-shift]

print(circular_shift(12, 1)) # "21"
print(circular_shift(12, 2)) # "12"
print(circular_shift(123456789, 3)) # "789123456"
print(circular_shift(123456789, 10)) # "987654321"