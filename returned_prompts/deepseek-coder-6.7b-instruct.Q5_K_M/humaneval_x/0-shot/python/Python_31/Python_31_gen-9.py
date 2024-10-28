
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = round(n ** 0.5)
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#test_is_prime.py
import unittest
from is_prime import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(101))
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(13441))
        self.assertTrue(is_prime(61))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
        
if __name__ == '__main__':
    unittest.main()

#test_is_prime_2.py
import unittest
from is_prime import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(103))
        self.assertFalse(is_prime(200))
        self.assertTrue(is_prime(113))
        self.assertFalse(is_prime(13441))
        self.assertTrue(is_prime(67))
        self.assertFalse(is_prime(41))
        self.assertFalse(is_prime(1))
        
if __name__ == '__main__':
    unittest.main()

#test_is_prime_3.py
import unittest
from is_prime import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime