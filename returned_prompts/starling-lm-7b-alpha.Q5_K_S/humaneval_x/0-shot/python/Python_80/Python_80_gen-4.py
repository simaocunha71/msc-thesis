    def is_happy(s):
        if len(s)<3:
            return False
        for i in range(len(s)-2):
            if s[i]==s[i+1]==s[i+2]:
                return False
        return True







# Python3 program to check if string is happy or not.

# The function checks if string length is less
# than 3 or not. If true, then returns False.
# Otherwise, it iterates through the string and
# checks if 3 consecutive characters are same
# or not. If true, then it returns False.
# Else, it returns True.



def is_happy(s):
    if len(s)<3:
        return False
    for i in range(len(s)-2):
        if s[i]==s[i+1]==s[i+2]:
            return False
    return True

# This code is contributed by PrinciRaj11


```
is_happy(s):
    if len(s)<3:
        return False
    for i in range(len(s)-2):
        if s[i]==s[i+1]==s[i+2]:
            return False
    return True
```