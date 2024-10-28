

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
    # Find the longest postfix that is a palindrome
    postfix = ''
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            postfix = string[:i]
            break
    if not postfix:
        return string
    # Find the prefix that comes before the postfix
    prefix = ''
    for i in range(len(string)):
        if string[i] in postfix:
            prefix = string[:i]
            break
    return prefix + postfix[::-1]


