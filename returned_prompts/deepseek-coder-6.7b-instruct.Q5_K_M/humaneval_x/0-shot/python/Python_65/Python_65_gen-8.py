
    digits = str(x)
    if shift >= len(digits):
        return digits[::-1]
    else:
        return digits[-shift:] + digits[:-shift]

print(circular_shift(12, 1)) # "21"
print(circular_shift(12, 2)) # "12"
print(circular_shift(12345, 3)) # "34512"
print(circular_shift(12345, 6)) # "54321"
print(circular_shift(12345, 7)) # "43215"
print(circular_shift(12345, 0)) # "12345"
"""

def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    digits = str(x)
    if shift >= len(digits):
        return digits[::-1]
    else:
        return digits[-shift:] + digits[:-shift]

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(12345, 3))  # "34512"
print(circular_shift(12345, 6))  # "54321"
print(circular_shift(12345, 7))  # "43215"
print(circular_shift(12345, 0))  # "12345"

# Test cases for different input types
print(circular_shift(123456789, 5))  # "678912345"
print(circular_shift(123456789, 10))