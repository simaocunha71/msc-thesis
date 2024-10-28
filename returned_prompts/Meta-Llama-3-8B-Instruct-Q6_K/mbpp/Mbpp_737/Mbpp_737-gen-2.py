```
import re

def check_str(s):
    if re.match('^[aeiouAEIOU]', s):
        return True
    else:
        return False
```
The function `check_str(s)` takes a string `s` as an argument. It uses the `re.match` function to check if the string starts with a vowel (both lowercase and uppercase). The regular expression `'^[aeiouAEIOU]'` matches any string that starts with a vowel. The `^` symbol indicates the start of the string, and `[aeiouAEIOU]` matches any vowel (both lowercase and uppercase). The function returns `True` if the string starts with a vowel, and `False` otherwise.

The unit test `assert check_str("annie")` ensures that the function works correctly. The string "annie" starts with the vowel "a", so the function should return `True`. If the function is implemented correctly, the unit test will pass. 