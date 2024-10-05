```
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True
```



Explanation:
The function `is_happy(s)` checks if the string `s` is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

The function first checks if the length of the string is less than 3. If it is, it returns `False` because a string of length less than 3 cannot be happy.

Then, it iterates over the string, checking every 3 consecutive letters. If any 3 consecutive letters are the same, it returns `False` because the string is not happy.

If the function finishes checking all the 3 consecutive letters and hasn't returned `False`, it means that every 3 consecutive letters are distinct, and the string is happy, so it returns `True`.