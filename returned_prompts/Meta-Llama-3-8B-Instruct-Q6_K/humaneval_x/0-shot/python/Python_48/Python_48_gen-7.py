```
def is_palindrome(text: str):
    return text == text[::-1]
```


Explanation:

The `is_palindrome` function takes a string `text` as input and checks if it is a palindrome or not. A palindrome is a string that reads the same backward as forward.

The function uses the slicing feature of Python to reverse the input string. The expression `text[::-1]` creates a new string that is the reverse of the original string. The `==` operator then checks if the original string is equal to its reverse. If they are equal, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`.

The unit tests provided in the problem demonstrate the expected behavior of the function. For example, an empty string is considered a palindrome, as is a string like `'aba'` that reads the same backward as forward. On the other hand, a string like `'zbcd'` is not a palindrome, as it does not read the same backward as forward.