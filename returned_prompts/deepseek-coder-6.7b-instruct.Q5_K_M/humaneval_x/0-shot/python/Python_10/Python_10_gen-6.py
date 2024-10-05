

    if is_palindrome(string):
        return string

    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()


This program works by scanning the string from the end towards the beginning looking for a palindrome. Once it finds one, it returns the string plus the reversed prefix of the non-palindromic part of the string. For instance, for the input string 'cata', it finds 'a' is a palindrome, so the function returns 'catac'.

This approach works because it allows us to find the shortest palindrome that begins with the input string. It does this by checking for palindromes from the end towards the start. The longest palindrome it will find is the entire string, so this will always return a palindrome.

The time complexity of this program is O(n^2) because of the nested loop, and the space complexity is O(n), because it creates a new string of size n in the worst case.
"""

#tests/test_palindrome.py
import pytest
from palindrome import is_palindrome, make_palindrome


@pytest.mark.parametrize("test_input,expected", [
    ("radar", True),
    ("python", False),
    ("", True),
    ("a", True),
    ("aa", True),
    ("ab", False),
])
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("", ""),
    ("a", "a"),
    ("cat", "catac"),
    ("cata", "catac"),
])
def test_make_palindrome(test_input, expected):
    assert make_palindrome(test_input) == expected

#tests/test_palindrome_efficiency.py
