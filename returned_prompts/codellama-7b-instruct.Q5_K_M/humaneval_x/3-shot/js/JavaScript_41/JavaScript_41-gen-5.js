

def is_palindrome(string: str) -> bool:
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
    if not string:
        return ''
    if is_palindrome(string):
        return string
    # Find the longest postfix of string that is a palindrome.
    postfix = ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            postfix = string[:i]
            break
    # Find the shortest prefix of string that is a palindrome.
    prefix = ''
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            prefix = string[i:]
            break
    return string + prefix[::-1]


def make_longest_palindrome(string: str) -> str:
    """ Find the longest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_longest_palindrome('')
    ''
    >>> make_longest_palindrome('cat')
    'catac'
    >>> make_longest_palindrome('cata')
    'catac'
    """
    if not string:
        return ''
    if is_palindrome(string):
        return string
    # Find the longest postfix of string that is a palind