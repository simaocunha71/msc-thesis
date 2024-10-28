
    largest_factor = 1
    i = 2

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i

    if n > 1:
        largest_factor = n

    return largest_factor


if __name__ == "__main__":
    import doctest

    doctest.testmod()

#tests/test_largest_prime_factor.py
import unittest
from largest_prime_factor import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)
        self.assertEqual(largest_prime_factor(66), 11)
        self.assertEqual(largest_prime_factor(9999), 37)
        self.assertEqual(largest_prime_factor(1257), 53)

if __name__ == "__main__":
    unittest.main()

#tests/test_largest_prime_factor_doctest.py
import doctest
from largest_prime_factor import largest_prime_factor

doctest.testmod(verbose=True)

#tests/test_largest_prime_factor_pytest.py
import pytest
from largest_prime_factor import largest_prime_factor

def test_largest_prime_factor():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(2048) == 2
    assert largest_prime_factor(66) == 11
    assert largest_prime_factor(9999) == 37
    assert largest_prime_factor(1257) == 53

if __name__ == "__main__":
    pytest.main()

#tests/test_largest_prime_factor_unittest.py
import unitt