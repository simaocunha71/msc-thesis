```
def remove_uppercase(s):
    return ''.join([c for c in s if c.islower()])
```



In this problem, we need to write a function that takes a string as input and returns a new string where all uppercase characters are removed. For example, if the input string is 'cAstyoUrFavoRitETVshoWs', the output should be 'cstyoravoitshos'.

The unit test `assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'` suggests that we need to remove all uppercase characters from the input string, not just the whole uppercase substrings.

We can achieve this using a list comprehension and the `islower()` method of the `str` class. The `islower()` method returns `True` if all characters in the string are lowercase, and `False` otherwise.

Here is the solution:
```
def remove_uppercase(s):
    return ''.join([c for c in s if c.islower()])
```
This function iterates over each character `c` in the input string `s`, and if the character is lowercase (i.e., `c.islower()` returns `True`), it includes the character in the output string. The `join()` method is used to concatenate the characters into a single string. The resulting string is the input string with all uppercase characters removed.