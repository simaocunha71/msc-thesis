```python


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
    def find_longest_palindromic_suffix(string: str) -> str:
        """ Returns the longest palindromic suffix of a supplied string """
        for i in range(len(string)):
            if is_palindrome(string[i:]):
                return string[i:]
        return ''

    if is_palindrome(string):
        return string

    longest_palindromic_suffix = find_longest_palindromic_suffix(string)
    prefix_to_append = string[:len(string) - len(longest_palindromic_suffix)][::-1]
    return string + prefix_to_append

```
