```
def is_palindrome(text: str):
    return text == text[::-1]
```
This function uses Python's slice notation to reverse the input string (`text[::-1]`) and then checks if the original string is equal to the reversed string. If they are equal, the function returns `True`, indicating that the input string is a palindrome. Otherwise, it returns `False`. The function works for empty strings, single-character strings, and strings of any length. For example, `is_palindrome('aba')` returns `True`, and `is_palindrome('zbcd')` returns `False`.