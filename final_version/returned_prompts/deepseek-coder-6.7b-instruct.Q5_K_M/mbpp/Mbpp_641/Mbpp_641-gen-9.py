def is_nonagonal(n):
    return n*(7*n - 5)//2

print(is_nonagonal(10))

#tests/test_nonagonal.py
import unittest
from nonagonal import is_nonagonal

class TestNonagonal(unittest.TestCase):

    def test_is_nonagonal(self):
        self.assertEqual(is_nonagonal(1), 1)
        self.assertEqual(is_nonagonal(2), 9)
        self.assertEqual(is_nonagonal(3), 20)
        self.assertEqual(is_nonagonal(4), 34)
        self.assertEqual(is_nonagonal(5), 51)
        self.assertEqual(is_nonagonal(10), 325)

if __name__ == '__main__':
    unittest.main()