
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

#test.py
import unittest
from prime import is_prime


class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(101), True)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(13441), True)
        self.assertEqual(is_prime(61), True)


if __name__ == "__main__":
    unittest.main()

#time_complexity.py
from prime import is_prime
import time

numbers = [13441, 61, 101, 11, 2, 1, 4, 6, 12, 14, 15, 21, 23, 27, 29, 31, 32, 37, 41, 43, 47, 53, 59, 67, 71, 73, 79, 83, 89, 97]

for n in numbers:
    start_time = time.time()
    print(f"Is {n} prime? {is_prime(n)}")
    print(f"Time taken: {time.time() - start_time}")

# The time complexity of the is_prime function is O