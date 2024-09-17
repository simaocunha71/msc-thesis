The problem is asking to find the minimum number of rotations required to get the same string. For example, if the string is "aaaa", we need to rotate it 1 time to get the same string.

Here is a Python function to solve this problem:

```
def find_Rotations(s):
    for i in range(1, len(s)):
        if s == s[i:]+s[:i]:
            return i
    return len(s)
```

This function works by iterating over the string and checking if the string is the same as the rotated string. If it is, it returns the number of rotations. If it's not, it continues to the next rotation. If it doesn't find a match, it returns the length of the string, which means the string needs to be rotated the full length of the string to get the same string.

The unit test `assert find_Rotations("aaaa") == 1` ensures that the function works correctly. For the string "aaaa", the function returns 1, which is the correct answer.