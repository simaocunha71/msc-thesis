```
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text == text[::-1]
```



Explanation:

The function `is_palindrome` takes a string `text` as input and returns a boolean value indicating whether the string is a palindrome or not.

A palindrome is a string that reads the same backward as forward. For example, 'aba' and 'aaaaa' are palindromes, while 'zbcd' is not.

The function uses slicing to reverse the string and compares it to the original string. If the reversed string is the same as the original string, then the string is a palindrome, and the function returns `True`. Otherwise, it returns `False`.

The unit tests provided demonstrate the expected behavior of the function. For example, an empty string is considered a palindrome, while 'zbcd' is not. The function correctly identifies these cases and returns the expected results.