```
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    """
    return text == text[::-1]
```



This function takes a string as input and returns True if it is a palindrome, False otherwise. A palindrome is a string that reads the same backward as forward. The function works by comparing the input string with its reverse using slicing (`text[::-1]`). If the two strings are the same, the function returns True; otherwise, it returns False. The provided unit tests demonstrate the function's correctness. For example, the test `is_palindrome('aba')` returns True because 'aba' is a palindrome, and the test `is_palindrome('zbcd')` returns False because 'zbcd' is not a palindrome.