```
def is_palindrome(text: str):
    return text == text[::-1]
```


Explanation:
The function `is_palindrome` takes a string as input and checks if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

The function uses Python's slice notation to reverse the input string (`text[::-1]`) and then compares it with the original string. If they are the same, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`.

The provided unit tests cover various cases, including an empty string, a palindrome with an odd number of characters, and a non-palindrome. The function passes all the tests.