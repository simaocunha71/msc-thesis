

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

    # Find the longest suffix of string that is a palindrome
    palindromic_suffix = ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            palindromic_suffix = string[:i]
            break

    # Find the longest prefix of string that is a palindrome
    palindromic_prefix = ''
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            palindromic_prefix = string[i:]
            break

    # Construct the resulting string
    return palindromic_suffix + palindromic_prefix[::-1]


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
    >>> make_pal