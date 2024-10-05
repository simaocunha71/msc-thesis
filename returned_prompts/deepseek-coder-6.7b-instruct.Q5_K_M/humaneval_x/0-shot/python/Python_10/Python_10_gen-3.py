

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if is_palindrome(string):
        return string

    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]


print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'


# Alternatively, you can use Python's built-in `reversed()` function to reverse the string and the `join()` method to concatenate the reversed string with the original one:

def make_palindrome(string: str) -> str:
    return string + ''.join(reversed(string))


print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catatc'
print(make_palindrome('cata'))  # 'cataatc'

Both solutions will return the same results, but the second one is a bit shorter.
"""


def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindrom