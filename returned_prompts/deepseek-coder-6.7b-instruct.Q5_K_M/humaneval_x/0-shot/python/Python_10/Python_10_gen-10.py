

def make_palindrome(string: str) -> str:
    if is_palindrome(string):
        return string
    else:
        for i in range(len(string)):
            if is_palindrome(string[i:]):
                return string + string[:i][::-1]
    return string + string[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()


The function `make_palindrome` first checks if the given string is a palindrome. If it is, it simply returns the string. Otherwise, it starts searching for a palindromic suffix in the string. Once it finds one, it appends to the string the reversed prefix of the string that comes before this palindromic suffix.

This algorithm works by iterating over the string and checking if the substring starting from the current position up to the end is a palindrome. If it is, we know we can create a palindrome by appending the reversed string prefix that comes before this palindromic substring. 

If no palindromic suffix is found after checking all substrings, that means the string is a palindrome itself, and we return the string.
"""

#tests/test_palindrome.py
import pytest
from palindrome import is_palindrome, make_palindrome


@pytest.mark.parametrize('test_input,expected', [
    ('', True),
    ('a', True),
    ('aa', True),
    ('ab', False),
    ('aba', True),
    ('abc', False),
])
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ('', ''),
    ('a', 'a'),
    ('aa', 'aa'),
    ('ab', 'aba'),
    ('aba', 'aba'),
    ('abc', 'abcba'),
])
def test_make_palindrome(test_input, expected):
    assert make_