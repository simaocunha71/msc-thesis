    # Unit digit
    unit_digit = lambda x: x % 10

    # Check if both numbers are positive
    if a < 0 or b < 0:
        raise ValueError('Both numbers must be positive')

    # Calculate the product of unit digits
    result = unit_digit(a) * unit_digit(b)

    return result

# Unit tests
assert multiply(148, 412) == 16
assert multiply(19, 28) == 72
assert multiply(2020, 1851) == 0
assert multiply(14, -15) == 20

# Test with negative numbers
try:
    multiply(-14, 15)
except ValueError as e:
    print(e)

# Test with zero
try:
    multiply(0, 10)
except ValueError as e:
    print(e)

# Test with very large numbers
try:
    multiply(10**20, 10**20)
except ValueError as e:
    print(e)

# Test with non-integer
try:
    multiply(14.8, 412)
except ValueError as e:
    print(e)

# Test with float result
try:
    multiply(1.2, 3.4)
except ValueError as e:
    print(e)






































































































































































