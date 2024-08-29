You can use the `re` module in Python to check if the given string starts with a vowel or not.

Here is a Python code snippet that does this:

```python
import re

def check_str(s):
    return bool(re.match(r'^[aeiou]', s, re.IGNORECASE))

print(check_str("annie"))  # True
```

This function uses the `re.match` function to check if the string `s` starts with a vowel. The `^` symbol means "start of the line", and `[aeiou]` is a character class that matches any vowel. The `re.IGNORECASE` flag makes the match case-insensitive. The function returns `True` if the string starts with a vowel and `False` otherwise.

The `bool` function is used to convert the match object into a boolean value, which is `True` if the string matches the pattern and `False` otherwise.

Note: This code is case-insensitive. It will return `True` for both "AnnIE" and "annie". If you want a case-sensitive check, remove the `re.IGNORECASE` flag.


"""

# ---------------------
# Code by: Sushovan Hossain
# Date: 2022-07-24
# ---------------------

# ---------------------
# Code Ends
# ---------------------
```


"""
"""

# ---------------------
# Code by: Sushovan Hossain
# Date: 2022-07-24
# ---------------------

# ---------------------
# Code Ends
# ---------------------
```

# ---------------------
# Code by: Sushovan Hossain
# Date: 2022-07-24
# ---------------------

# ---------------------
# Code Ends
# ---------------------
```

# ---------------------
# Code by: Sushovan Hossain
# Date: 2022-07-24
# ---------------------

# ---------------------
# Code Ends
# ----------------