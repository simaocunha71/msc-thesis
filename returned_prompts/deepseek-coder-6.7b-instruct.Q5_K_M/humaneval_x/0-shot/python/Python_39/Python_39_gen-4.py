
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fib(n):
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

    count = 0
    num = 0
    while count < n:
        num += 1
        if is_prime(fib(num)):
            count += 1

    return fib(num)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


This function works by defining two helper functions:

1. is_prime(num) checks if a number is prime or not.
2. fib(n) calculates the n-th Fibonacci number.

Then, in the main function, we iterate over the positive integers and check if the number is a Fibonacci number and a prime number. We increment our count each time we find a number that meets these criteria. We continue this process until we have found the n-th such number.

The time complexity of this solution is O(n^2), because for each number we are potentially calculating its Fibonacci value and checking if it's prime. The space complexity is O(1), because we are only storing a constant amount of variables.
"""

#tests/test_prime_fib.py
import unittest
from prime_fib import prime_fib


class TestPrimeFib(unittest.TestCase):

    def test_prime_fib(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)
        self.assertEqual(prime_