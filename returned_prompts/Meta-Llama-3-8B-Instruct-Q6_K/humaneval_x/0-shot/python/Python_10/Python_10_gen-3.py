Here is the solution:

```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
```


```python
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # Find the longest postfix of supplied string that is a palindrome
    postfix = string
    while not is_palindrome(postfix):
        postfix = postfix[1:]  # remove the first character
    # If the original string is already a palindrome, return it
    if postfix == string:
        return string
    # Calculate the prefix length
    prefix_len = len(string) - len(postfix)
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + string[:prefix_len][::-1]
```


The function `make_palindrome` generates the shortest palindrome that begins with a supplied string. It first finds the longest postfix of the supplied string that is a palindrome. Then, if the original string is already a palindrome, it returns the original string. Otherwise, it calculates the prefix length and appends to the end of the string the reverse of the string prefix that comes before the palindromic suffix. The function `is_palindrome` is used to check if a string is a palindrome. It returns `True` if the string is the same when reversed, and `False` otherwise. The unit tests show that the function `make_palindrome` works correctly for empty string and strings 'cat' and 'cata'. For example, `make_palindrome('cata')` returns `'catac'`.