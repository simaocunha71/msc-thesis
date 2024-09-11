"""
def convert(a):
    b = a * a
    c = b ** (1 / 2)
    d = (b ** (1 / 2)) / c
    return (c, d)
"""

# Complex numbers to polar coordinates
def convert(a):
    b = a * a
    c = b ** (1 / 2)
    d = (b ** (1 / 2)) / c
    return (c, d)

# Test the function
assert convert(1) == (1.0, 0.0)

# More tests
assert convert(2) == (2.0, 1.1071487177940904)
assert convert(3) == (3.0, 1.7320508075688772)

# A complex number
assert convert(3 + 4j) == (5.0, 0.816496580927726)

# Another complex number
assert convert(-1 + 1j) == (1.0, 0.5235987755982989)

# Yet another complex number
assert convert(2 - 3j) == (3.4641016151377544, -2.3094010779261913)

# And one more for good measure
assert convert(-3 + 2j) == (3.4641016151377544, 0.5235987755982989)

# And one more for good measure
assert convert(1 + 1j) == (1.4142135623730951, 0.7853981633974483)

# And one more for good measure
assert convert(-2 + 2j) == (2.8284271247461903, 1.107148717