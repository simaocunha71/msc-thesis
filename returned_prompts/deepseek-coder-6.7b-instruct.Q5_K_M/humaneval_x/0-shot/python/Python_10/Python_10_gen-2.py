

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

    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]


print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'


# Note: This solution is not the most efficient one, but it's easy to understand. It has time complexity O(n^2) due to the
# "is_palindrome" function which runs in O(n) time and is called in the "make_palindrome" function in a loop that runs in
# O(n) time. Therefore, the total time complexity of the program is O(n^2). It would be possible to optimize the solution to
# have a time complexity of O(n).


# Another approach could be to use a two-pointers technique to check if the string is a palindrome or not.
# This approach would have a time complexity of O(n).


# Note: The task description is not clear about the requirement to find a palindrome that starts with a given string.
# The provided solution assumes that the palindrome is a palindrome of the entire string, not a part of it.
# If the task is to find a palindrome that