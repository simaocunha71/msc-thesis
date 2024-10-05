Here is the implementation in Python:

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
    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
            return string + string[:i][::-1]
    return string
```

Note: The code above uses a simple algorithm to find the shortest palindrome that begins with a supplied string. This algorithm works by finding the longest postfix of the supplied string that is a palindrome, and then appending the reverse of the string prefix that comes before the palindromic suffix to the end of the string. If no such postfix exists, the original string is returned. This algorithm has a time complexity of O(n^2), where n is the length of the input string, due to the use of the `is_palindrome` function and the loop that finds the longest postfix. This is not the most efficient algorithm, but it is simple and easy to understand. For larger input strings, a more efficient algorithm may be needed.