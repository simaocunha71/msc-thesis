from typing import List


def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

# Alternatively, you can use the reduce function from the functools module:

from functools import reduce
from typing import List


def concatenate(strings: List[str]) -> str:
    return reduce(lambda x, y: x + y, strings)

# Or use a for loop:

from typing import List


def concatenate(strings: List[str]) -> str:
    result = ''
    for string in strings:
        result += string
    return result

# Or use a generator expression:

from typing import List


def concatenate(strings: List[str]) -> str:
    return ''.join(s for s in strings)
"""

#tests/test_exercises.py
import unittest
from exercises import *

class TestExercises(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(even_numbers(10), [0, 2, 4, 6, 8, 10])

    def test_positive_sum(self):
        self.assertEqual(positive_sum([1, -1, 2, -2]), 3)

    def test_reverse_string(self):
        self.assertEqual(reverse_string('abc'), 'cba')

    def test_palindrome(self):
        self.assertTrue(palindrome('abcba'))
        self.assertFalse(palindrome('abcd'))

    def test_unique_elements(self):
        self.assertEqual(set(unique_elements([1, 2, 2, 3, 4, 4, 4])), {1, 2, 3, 4})

    def test_concatenate(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')


if __name__ == '__main__':
    unittest.main()#chapter04/exercises.py
"""
