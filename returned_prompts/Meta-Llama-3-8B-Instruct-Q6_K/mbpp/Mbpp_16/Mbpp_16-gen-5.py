```
def text_lowercase_underscore(s):
    for i in range(1, len(s)):
        if s[i].islower() and s[i-1].islower() and s[i-1] != '_':
            return False
        if s[i] == '_' and not s[i-1].islower():
            return False
    return True
```



The function takes a string as input and checks if it contains sequences of lowercase letters joined with an underscore. It iterates over the string, checking each character and the previous one. If it finds a lowercase letter that is not preceded by an underscore, or an underscore that is not preceded by a lowercase letter, it returns False. If it checks the entire string and does not find any such sequences, it returns True. The unit test `assert text_lowercase_underscore("aab_cbbbc")==(True)` suggests that the function should return True for the input "aab_cbbbc" which is a sequence of lowercase letters joined with an underscore. 