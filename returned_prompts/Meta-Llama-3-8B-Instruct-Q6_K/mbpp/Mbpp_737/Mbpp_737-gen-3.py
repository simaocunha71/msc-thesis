```
import re

def check_str(s):
    if re.match('^[aeiouAEIOU]', s):
        return True
    else:
        return False
```


Explanation:
The function `check_str` takes a string `s` as input and checks whether it starts with a vowel or not using regular expression. 

The regular expression `^[aeiouAEIOU]` matches the start of a string (`^`) followed by any vowel (both lowercase and uppercase, `aeiouAEIOU`). 

If the string matches this pattern, the function returns `True`, indicating that the string starts with a vowel. If the string does not match, the function returns `False`. 

The unit test `assert check_str("annie")` checks if the string "annie" starts with a vowel, which it does (the first character 'a' is a vowel). The function correctly returns `True` for this test. 

This function is case-insensitive, meaning it will match both lowercase and uppercase vowels.  If you want to make it case-sensitive, you can remove the `AEIOU` part from the regular expression. 

This function does not handle non-string inputs. If you want to add error handling for non-string inputs, you can add a check at the beginning of the function to raise an error or return a default value if the input is not a string.  For example:

```
def check_str(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if re.match('^[aeiouAEIOU]', s):
        return True
    else:
        return False
```


This modified function will raise a `ValueError` if the input is not a string.  You can modify it to return a default value instead of raising an error if you prefer.  For example:

```
def check_str(s):
    if not isinstance(s, str):
        return False
    if re.match('^[aeiouAEIOU]', s):
        return True
    else:
        return False
```


This modified function will return `False` if the input is not a string.  You can choose the error handling approach that best fits your needs. 