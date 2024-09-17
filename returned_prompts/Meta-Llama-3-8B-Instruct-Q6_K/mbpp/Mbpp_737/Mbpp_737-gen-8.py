```
import re

def check_str(s):
    if re.match(r'^[aeiouAEIOU]', s):
        return True
    else:
        return False
```


The function `check_str` takes a string `s` as input and returns `True` if the string starts with a vowel (either lowercase or uppercase) and `False` otherwise. The regular expression `^[aeiouAEIOU]` matches if the string starts with a vowel. The `^` symbol means the start of the string, and the brackets `[]` contain the characters that the string can start with. The `re.match` function returns a match object if the string matches the regular expression, and `None` otherwise. The `if` statement checks if the result of `re.match` is truthy, and returns `True` if it is, and `False` otherwise. 

The unit test `assert check_str("annie")` checks if the function returns `True` for the string "annie", which starts with the vowel "a". The test will pass if the function is implemented correctly. 

Note: The regular expression `^[aeiouAEIOU]` can be simplified to just `^[aeiouAEIOU]` because the `^` symbol already means the start of the string, so there's no need to specify the start of the string again. However, I left it as `^[aeiouAEIOU]` for clarity. 

Also, it's worth noting that this function will return `False` for strings that are empty or only contain whitespace characters. If you want to handle these cases differently, you can add additional checks at the beginning of the function.  For example, you could return `True` for empty strings or strings containing only whitespace characters, or raise an error.  It depends on your specific requirements. 