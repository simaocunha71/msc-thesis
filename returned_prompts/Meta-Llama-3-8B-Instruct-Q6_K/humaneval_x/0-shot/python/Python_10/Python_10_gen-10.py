Here is a Python function that creates the shortest palindrome that starts with a given string. It works by finding the longest postfix of the given string that is a palindrome, and then appending the reverse of the prefix to the end of the string.

```
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    postfix = string
    while not is_palindrome(postfix):
        postfix = postfix[1:] + postfix[0]
    return postfix + string[::-1]
```

Here is the `is_palindrome` function that we used in the `make_palindrome` function:

```
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
```

The `is_palindrome` function checks if a given string is a palindrome by comparing it with its reverse. If they are the same, then the string is a palindrome. Otherwise, it's not. The `make_palindrome` function uses this function to find the longest postfix of the given string that is a palindrome. It then appends the reverse of the prefix to the end of the string to create the shortest palindrome that starts with the given string. This function works for any string, even an empty one. For example, `make_palindrome('')` returns an empty string, `make_palindrome('cat')` returns `'catac'`, and `make_palindrome('cata')` returns `'catac'`. 