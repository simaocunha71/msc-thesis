```
def odd_Equivalent(s, rotations):
    count = 0
    for _ in range(rotations):
        s = s[1:] + s[0]
    for char in s:
        if char == '1':
            count += 1
    return count
```


Explanation: 
This function takes a binary string `s` and the number of rotations `rotations` as input. It first rotates the string `rotations` times by shifting the characters from the end to the front. Then it counts the number of '1's in the resulting string, which represents the number of numbers with an odd value when rotating the binary string the given number of times. The unit test `assert odd_Equivalent("011001",6) == 3` ensures that the function returns the correct count. 





