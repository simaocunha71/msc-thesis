def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    x = str(x)
    if shift > len(x):
        return x[::-1]
    else:
        return x[-shift:] + x[:-shift]

print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"