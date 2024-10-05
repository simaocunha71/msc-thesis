```
def is_palindrome(text: str) -> bool:
    return text == text[::-1]
```


Explanation:
The function `is_palindrome` checks if a given string `text` is a palindrome. A palindrome is a string that reads the same backward as forward.

The function uses Python's slice notation `text[::-1]` to reverse the string. It then compares the original string with the reversed string using the `==` operator. If they are the same, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`.

The provided unit tests demonstrate the function's correctness:
- An empty string is considered a palindrome (`is_palindrome('')` returns `True`).
- The string `'aba'` is a palindrome (`is_palindrome('aba')` returns `True`).
- The string `'aaaaa'` is a palindrome (`is_palindrome('aaaaa')` returns `True`).
- The string `'zbcd'` is not a palindrome (`is_palindrome('zbcd')` returns `False`).
```python
assert is_palindrome('') == True
assert is_palindrome('aba') == True
assert is_palindrome('aaaaa') == True
assert is_palindrome('zbcd') == False
```


The function is simple, efficient, and easy to understand. It is also flexible and can handle strings of any length.