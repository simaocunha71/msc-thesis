
def circular_shift(x, shift):
    digits = str(x)
    if shift > len(digits):
        return digits[::-1]
    else:
        return digits[-shift:] + digits[:-shift]

# Test cases
print(circular_shift(12, 1) == "21")
print(circular_shift(12, 2) == "12")
print(circular_shift(123, 3) == "312")
print(circular_shift(12345, 100) == "54321")
print(circular_shift(10000000000, 100000) == "0000000001")



# Other solutions
# Other solutions
from math import log, floor

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
    d = floor(log(x) / log(10)) + 1
    if d < shift:
        return s[shift:] + s[:shift]
    else:
        return s[-shift:] + s[:-shift]

# Test cases
print(circular_shift(12, 1) == "21")
print(circular_shift(12, 2) == "12")
print(circular_shift(123, 3) == "312")
print(circular_shift(12345, 100) == "54321")
print(circular_shift(10000000000, 100000) == "0000000001")



from math import