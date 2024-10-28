

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if is_palindrome(string):
        return string

    # Find the longest postfix of supplied string that is a palindrome.
    palindromic_suffix = ''
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            palindromic_suffix = string[:i]
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return string + string[:len(palindromic_suffix) - 1][::-1]


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertFalse(is_palindrome('cat'))
        self.assertTrue(is_palindrome('catac'))
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('aa'))
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('abba'))
        self.assertTrue(is_palindrome('abcdcba'))
        self.assertTrue(is_palindrome('abcde'))
        self.assert