```
def remove_lowercase(s):
    return ''.join(c for c in s if not c.islower())
```



This function takes a string `s` as input and returns a new string where all lowercase characters are removed. The `islower()` method is used to check if a character is lowercase, and the `join()` method is used to concatenate the characters that are not lowercase into a new string.

The unit test `assert remove_lowercase("PYTHon")==('PYTH')` ensures that the function works correctly. It checks that the output of the function `remove_lowercase("PYTHon")` is `'PYTH'`, which means that all lowercase characters ('o') have been removed from the input string. 