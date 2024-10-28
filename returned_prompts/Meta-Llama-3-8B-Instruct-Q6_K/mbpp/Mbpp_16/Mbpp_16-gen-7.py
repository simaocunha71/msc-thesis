```
def text_lowercase_underscore(s):
    s = s.replace("_", "")
    return s.islower()
```
The problem is asking you to write a function that checks if a given string contains sequences of lowercase letters joined with an underscore. The function should return True if the string meets the condition and False otherwise.

The provided unit test `assert text_lowercase_underscore("aab_cbbbc")==(True)` suggests that the function should return True for the input string "aab_cbbbc". This implies that the function should remove the underscores from the string and check if the resulting string is in lowercase.

Here is a Python solution that meets the condition:
```
def text_lowercase_underscore(s):
    s = s.replace("_", "")
    return s.islower()
```
This function replaces all underscores in the input string with an empty string, effectively removing them. Then, it checks if the resulting string is in lowercase using the `islower()` method. If the string is in lowercase, the function returns True; otherwise, it returns False.