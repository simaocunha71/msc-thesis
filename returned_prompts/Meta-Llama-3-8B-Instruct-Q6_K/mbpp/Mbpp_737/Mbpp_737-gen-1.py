```
import re

def check_str(s):
    if re.match('^[aeiouAEIOU]', s):
        return True
    else:
        return False
```


Explanation: 
In this problem, we need to write a function that checks if a given string is starting with a vowel or not. A vowel is defined as 'a', 'e', 'i', 'o', 'u' or 'A', 'E', 'I', 'O', 'U'.

The unit test provided is `assert check_str("annie")`. This means the function should return `True` for the string "annie" because it starts with a vowel 'a'.

To solve this problem, we can use the `re` module in Python, which provides support for regular expressions. We can use the `re.match` function to check if the string starts with a vowel. The pattern `^[aeiouAEIOU]` matches any string that starts with a vowel. The `^` symbol means the start of the string, and `[aeiouAEIOU]` is a character class that matches any of the characters inside it.

Here is the Python function that implements this:

```
import re

def check_str(s):
    if re.match('^[aeiouAEIOU]', s):
        return True
    else:
        return False
```

This function takes a string `s` as input, and returns `True` if the string starts with a vowel, and `False` otherwise. The `re.match` function returns a match object if the string starts with a vowel, and `None` otherwise. The `if` statement checks if the match object is not `None`, and returns `True` if it is not, and `False` otherwise. If the string does not start with a vowel, the function returns `False`. 