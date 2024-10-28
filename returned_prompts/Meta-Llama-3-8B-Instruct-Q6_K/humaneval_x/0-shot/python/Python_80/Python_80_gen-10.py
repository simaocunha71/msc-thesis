```
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(0, len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True
```



Explanation:

The function `is_happy(s)` checks if the string `s` is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

The function first checks if the length of the string is less than 3. If it is, the function returns `False` because a string with a length less than 3 cannot be happy.

Then, the function iterates over the string with a loop that ranges from the first character to the third last character. For each character, it checks if the character is the same as the next one or the one after that, or if the next one is the same as the one after that. If any of these conditions are true, the function returns `False` because the string is not happy.

If the function has not returned `False` after checking all characters, it means that every 3 consecutive letters are distinct, so the function returns `True` to indicate that the string is happy.