```
def odd_Equivalent(s, rotations):
    count = 0
    for _ in range(rotations):
        s = s[1:] + s[0]
    for i in range(len(s)):
        if int(s[i]) % 2 != 0:
            count += 1
    return count
```


The function takes a binary string `s` and an integer `rotations` as input. It first rotates the binary string `rotations` times. Then, it counts the number of characters in the rotated string that have an odd value when converted to an integer. The function returns this count. The unit test `assert odd_Equivalent("011001",6) == 3` ensures that the function works correctly.