```
def find_Rotations(s):
    n = len(s)
    for i in range(1, n):
        if s[i:] + s[:i] == s:
            return i
    return None
```
The function `find_Rotations(s)` takes a string `s` as input and returns the minimum number of rotations required to get the same string. If no rotation is found, it returns `None`.

The function iterates over the string `s` and checks if the string is the same as its rotated version. If a rotation is found, it returns the number of rotations. If no rotation is found after checking all possibilities, it returns `None`.

For example, if the input is "aaaa", the function will return 1 because the string "aaaa" is the same as its rotated version "aaaa" after 1 rotation.

The unit test `assert find_Rotations("aaaa") == 1` ensures that the function works correctly for the input "aaaa". The function should return 1, which is the minimum number of rotations required to get the same string.