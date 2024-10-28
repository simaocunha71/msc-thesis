from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""
The code provided above defines a function named filter_by_substring which takes a list of strings and a substring as arguments. It returns a new list containing only those strings from the input list that contain the specified substring.

The function uses a list comprehension to iterate over the input list of strings and includes only those strings in the new list that contain the given substring.

The doctest module is used to provide a simple way of defining test cases in the form of documentation strings. The doctest.testmod() function is used to run these test cases, and if all of the test cases pass, the function returns a (0, 0, 0, 0) tuple. If any of the test cases fail, the function returns a tuple representing the number of failed test cases, the number of tests that didn't run, the number of tests that did run, and the total number of tests.

The doctest module is a part of the Python standard library, so it doesn't need to be installed separately.
"""

#filter_by_substring_test.py
import unittest
from filter_by_substring import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    def test_filter_by_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])
        self.assertEqual(filter_by_substring(['hello', 'world', 'python', 'programming'], 'o'), ['hello', 'programming'])
        self.assertEqual(filter_by_substring(['apple', 'banana', 'cherry', 'date'], 'z'), [])
        self.assertEqual(filter_by_substring([], 'test'), [])

if __name__ == '__main__':
    unittest.main()
