```
def is_palindrome(text: str):
    return text == text[::-1]
```

This function checks if the given string is a palindrome by comparing it with its reverse. The `text[::-1]` expression returns a reversed copy of the string. If the original string is the same as its reverse, then it's a palindrome, and the function returns `True`. Otherwise, it returns `False`. The function works correctly even for empty strings, which are considered to be palindromes.