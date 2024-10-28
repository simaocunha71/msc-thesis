```
def find_Rotations(s):
    rotations = 0
    for i in range(1, len(s)):
        if s == s[i:] + s[:i]:
            return i
    return len(s)
```


The function `find_Rotations` takes a string `s` as input and returns the minimum number of rotations required to get the same string. The function iterates over the string and checks if the string is equal to its rotation. If a rotation is found, the function returns the number of rotations. If no rotation is found, the function returns the length of the string.

The unit test `assert find_Rotations("aaaa") == 1` checks if the function returns the correct result for the string "aaaa". The string "aaaa" is the same when rotated by 1 position, so the function should return 1. The test passes because the function returns 1 for the input "aaaa".