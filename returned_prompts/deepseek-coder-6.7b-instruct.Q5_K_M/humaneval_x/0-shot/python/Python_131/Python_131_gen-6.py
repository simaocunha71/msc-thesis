
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = [int(d) for d in str(n)]
    odd_digits = [d for d in digits if d % 2 != 0]
    if not odd_digits:
        return 0
    else:
        product = 1
        for d in odd_digits:
            product *= d
        return product

#tests/test_digits.py
import pytest
from digits import digits

def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(97531) == 25
    assert digits(2468) == 0
    assert digits(802040) == 0
    assert digits(13579) == 105
    assert digits(942010492) == 49
    assert digits(2222222) == 0
    assert digits(1111111) == 1
    assert digits(9576428) == 352
    assert digits(64286) == 128
    assert digits(1111111111) == 1
    assert digits(123456789) == 0
    assert digits(987654321) == 729