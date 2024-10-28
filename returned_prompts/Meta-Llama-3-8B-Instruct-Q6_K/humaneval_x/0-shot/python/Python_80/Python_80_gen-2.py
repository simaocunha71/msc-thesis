```
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True
```


This solution iterates over the string and checks if any three consecutive characters are the same. If it finds any, it returns False. If it doesn't find any, it returns True. The condition for returning False is also added for strings with length less than 3. The string is considered not happy if its length is less than 3. This is because the problem statement requires the length to be at least 3. 

This solution works in O(n) time complexity, where n is the length of the string. The space complexity is O(1) as it only uses a constant amount of space to store the string and the variables. 

Note: This solution assumes that the input string is not None and does not contain any non-string values. If the input string can be None or contain non-string values, additional checks should be added to handle these cases. 





