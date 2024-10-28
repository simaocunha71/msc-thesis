```
def find_Rotations(s):
    rotations = 0
    while True:
        if s == s[1:] + s[0]:
            return rotations + 1
        s = s[1:] + s[0]
        rotations += 1
```
Explanation: 
This function works by continuously rotating the string and checking if it is equal to the original string. The number of rotations required to get the same string is the minimum number of rotations required. The unit test `assert find_Rotations("aaaa") == 1` ensures that the function returns the correct result for the input "aaaa". 

This function has a time complexity of O(n) where n is the length of the string, as it iterates over the string once for each rotation. The space complexity is O(1) as it only uses a constant amount of space to store the string and the rotation count. 





