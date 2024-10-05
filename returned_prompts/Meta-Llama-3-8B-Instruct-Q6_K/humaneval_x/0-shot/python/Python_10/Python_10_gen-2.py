Here is the solution in Python:

```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # Check if the string is already a palindrome
    if is_palindrome(string):
        return string

    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string), -1, -1):
        postfix = string[i:]
        if is_palindrome(postfix):
            break

    # Append to the end of the string the reverse of the string prefix that comes before the palindromic suffix
    return string + postfix[::-1]
```


This code defines two functions, `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome by comparing it with its reverse. The `make_palindrome` function finds the shortest palindrome that begins with a supplied string. It does this by finding the longest postfix of the string that is a palindrome and appending the reverse of the string prefix that comes before the palindromic suffix. If the original string is already a palindrome, the function returns the original string. If not, the function finds the longest postfix of the string that is a palindrome and returns the string with the postfix and the reverse of the string prefix appended to it. The time complexity of the `make_palindrome` function is O(n), where n is the length of the input string. The space complexity is O(1), since it only uses a constant amount of space.