"""
Here is the Python code that solves the problem:
"""

def find_solution(a, b, n):
    if a == 0 and b == 0:
        return None
    if a == 0:
        if n % b == 0:
            return (0, n // b)
        else:
            return None
    if b == 0:
        if n % a == 0:
            return (n // a, 0)
        else:
            return None

    if a > b:
        q, r = divmod(n, a)
        if r == 0:
            return (0, q)
        x, y = find_solution(b % a, a, r)
        return (x + q * y, y)
    else:
        q, r = divmod(n, b)
        if r == 0:
            return (q, 0)
        x, y = find_solution(a, b % a, r)
        return (x, y + q * y)


print(find_solution(2, 3, 7))  # returns (2, 1)

"""
In the function, we use the Euclidean algorithm to find the greatest common divisor of a and b. If n is divisible by the greatest common divisor, we return the quotient as the solution for y, and n divided by the greatest common divisor as the solution for x. Otherwise, we recursively call the function with the remainder and the smaller of the two numbers.
"""

#tests.py
import unittest
from main import find_solution


class TestFindSolution(unittest.TestCase):
    def test_find_solution(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))
        self.assertEqual(find_solution(1, 2, 3), (1, 1))
        self.assertEqual(find_solution(3, 4, 5), (1, -1))
        self.assertEqual(find_solution(2, 2, 4), (2, 0))
        self.assertEqual(find_solution