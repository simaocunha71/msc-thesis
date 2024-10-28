```
def remove_lowercase(s):
    return ''.join([c for c in s if c.isupper()])
```
The problem is asking to create a function that takes a string as input and returns a new string with all lowercase characters removed. The function should only keep the uppercase characters from the original string. 

The provided unit test `assert remove_lowercase("PYTHon")==('PYTH')` suggests that the function should remove the 'o' from the string "PYTHon" and return the remaining string "PYTH".

Here is a Python solution using a list comprehension and the `isupper()` method. The function iterates over each character in the input string, checks if the character is uppercase using `isupper()`, and if it is, adds it to a new list. The list is then joined into a string using the `join()` method. 

This solution passes the provided unit test. 

Here is the code:
```
def remove_lowercase(s):
    return ''.join([c for c in s if c.isupper()])
``` 





