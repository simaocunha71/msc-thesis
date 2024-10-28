```
import re

def check_str(s):
    return bool(re.match(r'^[aeiouAEIOU]', s))
```
The function `check_str` takes a string `s` as input and returns `True` if the string starts with a vowel (both lowercase and uppercase) and `False` otherwise. The regular expression `r'^[aeiouAEIOU]'` matches the string if it starts with a vowel. The `^` symbol denotes the start of the string and the `[aeiouAEIOU]` part matches any vowel. The `re.match` function returns a match object if the string matches the regular expression, and `None` otherwise. The `bool` function converts this to `True` or `False`. 

For example, `check_str("annie")` returns `True` because "annie" starts with "a", which is a vowel. `check_str("hello")` returns `False` because "hello" does not start with a vowel. 