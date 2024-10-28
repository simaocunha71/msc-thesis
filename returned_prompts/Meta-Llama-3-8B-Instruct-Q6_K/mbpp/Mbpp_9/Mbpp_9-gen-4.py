```
def find_Rotations(s):
    for i in range(1, len(s)):
        if s == s[i:] + s[:i]:
            return i
    return 0
```
The problem is asking for the minimum number of rotations (greater than 0) required to get the same string. This means we need to find the smallest positive integer `n` such that the string `s` rotated `n` times becomes the same as the original string.

For example, if the input string is "aaaa", the function should return 1 because rotating "aaaa" by 1 position gives us the same string back.

The unit test `assert find_Rotations("aaaa") == 1` helps us to understand the problem better. It indicates that the function should return the smallest positive integer `n` such that `s` rotated `n` times becomes the same as the original string.

Here is the Python function that solves the problem:

```
def find_Rotations(s):
    for i in range(1, len(s)):
        if s == s[i:] + s[:i]:
            return i
    return 0
```

This function iterates over the string `s` and checks if the string is the same as the rotated string. If it finds a match, it returns the rotation number. If no match is found, it returns 0. The unit test `assert find_Rotations("aaaa") == 1` passes with this function. 