

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

    prefix = ''
    suffix = string
    while not is_palindrome(suffix):
        suffix = suffix[:-1]

    return prefix + suffix + suffix[::-1]


def test_make_palindrome_1():
    """ Test for the first example from the problem statement """
    assert make_palindrome("") == ""


def test_make_palindrome_2():
    """ Test for the second example from the problem statement """
    assert make_palindrome("cat") == "catac"


def test_make_palindrome_3():
    """ Test for the third example from the problem statement """
    assert make_palindrome("cata") == "catac"


def test_make_palindrome_4():
    """ Test for the fourth example from the problem statement """
    assert make_palindrome("catac") == "catac"


def test_make_palindrome_5():
    """ Test for the fifth example from the problem statement """
    assert make_palindrome("catacata") == "catacata"


def test_make_palindrome_6():
    """ Test for the sixth example from the problem statement """
    assert make_palindrome("catcat") == "catcatcatcat"


def