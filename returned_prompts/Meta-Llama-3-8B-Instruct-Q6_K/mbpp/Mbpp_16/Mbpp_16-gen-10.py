```
def text_lowercase_underscore(s):
    import re
    return bool(re.search(r"[a-z]+_", s))
```





The function `text_lowercase_underscore` takes a string `s` as input and returns `True` if the string contains sequences of lowercase letters joined with an underscore, and `False` otherwise.

The regular expression `[a-z]+_` matches one or more lowercase letters (`[a-z]+`) followed by an underscore (`_`). The `re.search` function returns a match object if the pattern is found in the string, or `None` otherwise. The `bool` function is used to convert the result to a boolean value.

The unit test `assert text_lowercase_underscore("aab_cbbbc")==(True)` ensures that the function returns the correct result for the input string `"aab_cbbbc"`.