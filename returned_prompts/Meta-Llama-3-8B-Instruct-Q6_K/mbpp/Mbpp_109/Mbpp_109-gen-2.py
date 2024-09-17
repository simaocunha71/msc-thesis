```
def odd_Equivalent(s, n):
    count = 0
    for i in range(n):
        s = s[1:] + s[0]
        odd = False
        for char in s:
            if char == '1':
                odd = not odd
        if odd:
            count += 1
    return count
```


The problem is asking to write a function that takes a binary string and an integer as input, and returns the number of times the string has an odd number of 1's when rotated the given number of times. The rotation operation is done by moving the first character to the end of the string.

The unit test `assert odd_Equivalent("011001",6) == 3` helps to understand the problem better. It shows that the string "011001" has 3 rotations that have an odd number of 1's when rotated 6 times. 

Here's the solution: The function iterates over the given number of rotations, each time rotating the string and checking if it has an odd number of 1's. If it does, it increments the count. Finally, it returns the count. 

The time complexity of this solution is O(n*m), where n is the given number of rotations and m is the length of the string. This is because in the worst case, the function needs to iterate over the string for each rotation. The space complexity is O(1), as it only uses a constant amount of space to store the count and the rotated string. 