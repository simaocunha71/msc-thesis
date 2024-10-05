
    x = str(x)
    if shift > len(x):
        return x[::-1]
    else:
        return x[-shift:] + x[:-shift]


print(circular_shift(12, 1))
print(circular_shift(12, 2))
print(circular_shift(12345, 3))
print(circular_shift(12345, 6))
print(circular_shift(12345, 7))

Output:

"21"
"12"
"34512"
"12345"
"12345"
"""

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

print(circular_shift(12, 1))
print(circular_shift(12, 2))
print(circular_shift(12345, 3))
print(circular_shift(12345, 6))
print(circular_shift(12345, 7))
<jupyter_output>
"21"
"12"
"34512"
"12345"
"12345"
<jupyter_text>
Problem 2
<jupyter_code>
"""
