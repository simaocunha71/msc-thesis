```
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(0, len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True
```


Here, we use a for loop to iterate over the string. For each position, we check if the current character is the same as the next one, or the current character is the same as the one after the next one, or the next character is the same as the one after the next one. If any of these conditions are met, we return False, because the string is not happy. If we reach the end of the loop without returning False, we return True, because the string is happy. This function will return False if the string is shorter than 3 characters, because a happy string must have at least 3 characters.