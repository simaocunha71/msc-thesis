Here is the solution:

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
    # reverse the string
    reversed_string = string[::-1]
    # iterate over the reversed string and the original string
    for i in range(len(string)):
        # if the prefix of the reversed string is equal to the postfix of the original string
        if reversed_string[i:] == string[len(string) - i:]:
            # return the original string and the prefix of the reversed string
            return string + reversed_string[i:]
    # if no palindrome is found, return the original string and the reversed string
    return string + reversed_string
```
The provided solution consists of two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome by comparing it with its reverse. The `make_palindrome` function generates the shortest palindrome that begins with a supplied string. It does this by finding the longest postfix of the supplied string that is a palindrome, and then appending the reverse of the string prefix that comes before the palindromic suffix to the end of the string.

The function `make_palindrome` works as follows:
- It first reverses the input string.
- Then, it iterates over the reversed string and the original string.
- For each position `i` in the reversed string, it checks if the prefix of the reversed string (from position `i` to the end) is equal to the postfix of the original string (from position `len(string) - i` to the end).
- If it finds such a position `i`, it returns the original string and the prefix of the reversed string.
- If no such position `i` is found, it returns the original string and the reversed string.

This solution has a time complexity of O(n), where n is the length of the input string. This is because it iterates over the input string once. The space complexity is O(n) as well, as it stores the reversed string.