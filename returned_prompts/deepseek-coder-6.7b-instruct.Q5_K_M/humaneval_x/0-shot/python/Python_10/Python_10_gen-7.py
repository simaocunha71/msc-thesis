

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
    else:
        for i in range(len(string)):
            if is_palindrome(string[i:]):
                return string + string[:i][::-1]


print(make_palindrome(''))
print(make_palindrome('cat'))
print(make_palindrome('cata'))

The function `is_palindrome` checks if a given string is a palindrome by comparing it to its reverse. The function `make_palindrome` checks for the longest postfix of the given string that is a palindrome. If no such postfix exists, it appends the reverse of the prefix to the string.

The time complexity of the function `make_palindrome` is O(n^2) because in the worst case, it needs to check every prefix of the string to see if it is a palindrome. The space complexity is O(n) because it creates a new string that is the reversed prefix.

This solution may not be the most efficient for very long strings, because it checks every prefix of the string. A more efficient solution would use a different algorithm that finds the shortest palindrome in linear time.
