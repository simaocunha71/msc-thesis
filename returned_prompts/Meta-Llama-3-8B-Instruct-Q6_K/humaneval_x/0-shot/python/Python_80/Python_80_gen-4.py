```
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s)-2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True
```


```
# Testing the function
print(is_happy("a"))  # False
print(is_happy("aa"))  # False
print(is_happy("abcd"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))  # True
print(is_happy("xyy"))  # False
```


This function checks if the string has a length of at least 3 and every 3 consecutive characters are distinct. If any of the conditions fail, it returns False. If the string meets the conditions, it returns True. The function iterates over the string and checks for any consecutive characters that are the same. If it finds any, it immediately returns False. If it doesn't find any, it returns True after checking the entire string. The test cases at the end demonstrate the function's behavior on different input strings.