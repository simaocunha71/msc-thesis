```
def remove_lowercase(s):
    return ''.join(c for c in s if c.isupper())
```
This function uses a generator expression to iterate over each character `c` in the input string `s`. It uses the `isupper()` method to check if the character is uppercase, and if it is, it includes it in the resulting string. The `join()` method is then used to concatenate the uppercase characters into a single string.

The unit test `assert remove_lowercase("PYTHon")==('PYTH')` ensures that the function works correctly by checking that the lowercase substring "on" is removed from the input string "PYTHon", leaving only the uppercase substring "PYTH".