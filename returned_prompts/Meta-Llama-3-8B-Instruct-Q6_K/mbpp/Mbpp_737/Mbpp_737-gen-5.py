```
import re

def check_str(s):
    pattern = re.compile('^[aeiouAEIOU]')  # ^ means start of the string
    if pattern.match(s):
        return True
    else:
        return False
```


The function `check_str(s)` checks if a given string `s` starts with a vowel or not. It uses a regular expression pattern `^[aeiouAEIOU]` which means the string should start with any of the characters 'a', 'e', 'i', 'o', 'u', or 'A', 'E', 'I', 'O', 'U'. If the string matches this pattern, it returns `True` otherwise `False`. The unit test `assert check_str("annie")` passes as the string "annie" starts with the vowel 'a'. 

Note that the `^` character in the regular expression is used to specify the start of the string, so the pattern `^[aeiouAEIOU]` checks if the string starts with a vowel. If the string starts with any other character, the pattern will not match and the function will return `False`. 

The `re.compile()` function compiles the regular expression pattern into a regular expression object, which can be used for matching using its `match()` method. The `match()` method returns a match object if the string matches the pattern, otherwise `None`. In this function, we use the `if` statement to check if the match object is not `None`, which means the string matches the pattern. If the string matches the pattern, the function returns `True`; otherwise, it returns `False`. 





Python code:
```
import re

def check_str(s):
    pattern = re.compile('^[aeiouAEIOU]')  # ^ means start of the string
    if pattern.match(s):
        return True
    else:
        return False

assert check_str("annie")
```



When you run the code, it will return `True` for the input "annie" because it starts with the vowel 'a'. If you input a string that does not start with a vowel, it will return `False`. For example, `check_str("hello")` will return `False` because "hello" does not start with a vowel.