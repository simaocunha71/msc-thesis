```
def remove_uppercase(s):
    return ''.join([c for c in s if c.islower()])
```
The problem is asking you to create a function that takes a string as input and returns a new string where all uppercase characters have been removed.

The unit test provided, `assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'`, helps clarify the problem by showing that the function should return a new string where all uppercase characters have been replaced with their lowercase equivalents.

Here is the solution in Python:
```
def remove_uppercase(s):
    return ''.join([c for c in s if c.islower()])
```
This function uses a list comprehension to iterate over each character `c` in the input string `s`. It checks if the character is lowercase using the `islower()` method, and if it is, it includes it in the new string. The `join()` method is then used to concatenate the characters into a single string. The resulting string has all uppercase characters removed.