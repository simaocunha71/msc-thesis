```
def text_lowercase_underscore(s):
    return all(c.islower() or c == '_' for c in s)
```


The function `text_lowercase_underscore(s)` checks if the input string `s` contains sequences of lowercase letters joined with an underscore. It does this by iterating over each character `c` in the string and checking if it is a lowercase letter (`c.islower()`) or an underscore (`c == '_`'). The `all()` function then checks if all characters in the string satisfy this condition. If they do, the function returns `True`; otherwise, it returns `False`.

The unit test `assert text_lowercase_underscore("aab_cbbbc")==(True)` ensures that the function correctly identifies strings that contain sequences of lowercase letters joined with an underscore. In this case, the input string `"aab_cbbbc"` is correctly identified as satisfying the condition, so the function returns `True`.