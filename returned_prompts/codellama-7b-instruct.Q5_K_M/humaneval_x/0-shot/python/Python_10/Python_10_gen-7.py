

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
    # find the longest postfix of string that is a palindrome
    palindromic_suffix = ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i:]):
            palindromic_suffix = string[i:]
            break
    # find the prefix that comes before the palindromic suffix
    prefix = string[:-len(palindromic_suffix)]
    # create the palindrome by appending the reversed prefix to the end of the palindromic suffix
    return palindromic_suffix + prefix[::-1]


def test_palindrome():
    assert is_palindrome('')
    assert is_palindrome('cat')
    assert is_palindrome('catac')
    assert is_palindrome('catcatac')
    assert not is_palindrome('catcata')


def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
    assert make_palindrome('catcata') == 'catacatac'


if __name__ == '__main__':
    test