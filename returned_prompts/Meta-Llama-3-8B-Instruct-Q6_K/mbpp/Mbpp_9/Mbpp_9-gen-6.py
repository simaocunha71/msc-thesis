The problem is asking to write a function that finds the minimum number of rotations required to get the same string. For example, if the input string is "aaaa", the function should return 1 because one rotation of the string "aaaa" will give the same string.

Here is a python function to solve this problem:

```
def find_Rotations(s):
    for i in range(1, len(s)):
        if s == s[i:] + s[:i]:
            return i
    return len(s)
```

This function works by iterating over the string and checking if the string is equal to itself after rotation. If it is, it returns the number of rotations. If not, it returns the length of the string, which means the string is the same as itself after rotation, so the minimum number of rotations is 1.

For example, if the input string is "aaaa", the function will return 1 because one rotation of the string "aaaa" will give the same string. The unit test `assert find_Rotations("aaaa") == 1` will pass. 