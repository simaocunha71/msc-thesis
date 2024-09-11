"""
Here's a Python function that uses the `re` module to check if a string starts with a vowel using a regular expression:

```python
import re

def check_str(s):
    pattern = r'^[aeiou]'
    return re.match(pattern, s) is not None
```

In this function, the regular expression pattern `^[aeiou]`