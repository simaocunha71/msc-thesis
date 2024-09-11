"""
def left_rotate(number, d):
    left_bits = (number & (2 ** d - 1)) << (32 - d)
    right_bits = (number >> d)
    return left_bits | right_bits
"""

def left_rotate(number, d):
    return (number << d) | (number >> (32 - d))

def test_left_rotate():
    assert left_rotate(16, 2) == 64
    assert left_rotate(2, 5) == 34
    assert left_rotate(1, 0) == 1
    assert left_rotate(1, 1) == 2
    assert left_rotate(1, 32) == 2147483648
    assert left_rotate(2147483647, 1) == 2147483646

test_left_rotate()

"""
def left_rotate(number, d):
    left_bits = (number & (2 ** d - 1)) << (32 - d)
    right_bits = (number >> d)
    return left_bits | right_bits
"""

def left_rotate(number, d):
    return (number << d) | (number >> (32 - d))

def test_left_rotate():
    assert left_rotate(16, 2) == 64
    assert left_rotate(2, 5) == 34
    assert left_rotate(1, 0) == 1
    assert left_rotate(1, 1) == 2
    assert left_rotate(1, 32) == 2147483648
    assert left_rotate(2147483647, 1) == 2147483646

test_left_rotate()

"""
def left_rotate(number, d):
    left_bits = (number & (2 ** d - 1)) << (32 - d)
    right_bits = (number >> d)
    return left_bits | right_bits
"""