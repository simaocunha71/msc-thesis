```
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True
```


Note: The function checks if the length of the string is less than 3, if so, it returns False. Then it iterates over the string and checks if any 3 consecutive letters are the same. If it finds any, it returns False. If it doesn't find any, it returns True. This function considers a string as happy if every 3 consecutive letters are distinct. The time complexity is O(n) and the space complexity is O(1), where n is the length of the string.