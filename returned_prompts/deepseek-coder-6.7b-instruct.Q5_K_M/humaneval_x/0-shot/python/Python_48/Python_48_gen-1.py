

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text == text[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

#test_is_palindrome.py
import unittest
from main import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aaaaa'))
        self.assertFalse(is_palindrome('zbcd'))


if __name__ == '__main__':
    unittest.main()

#test_main.py
import unittest
from main import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aaaaa'))
        self.assertFalse(is_palindrome('zbcd'))


if __name__ == '__main__':
    unittest.main()# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-reversion-compare',
    version='0.0.1',
    description='Reversion Compare',
    long_description=open('README.rst').read(),
    author='Roman Haritonov',
    author_email='roman@flowrl.com',
    url