
    # Check for edge cases
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#test_prime_numbers.py
import unittest
from prime_numbers import is_prime


class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(61))
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13441))


if __name__ == "__main__":
    unittest.main()#bubble_sort.py
