```
def odd_Equivalent(s, n):
    count = 0
    for _ in range(n):
        s = ''.join('1' if c == '0' else '0' for c in s)
    for c in s:
        if c == '1':
            count += 1
    return count
```


The function `odd_Equivalent` takes a binary string `s` and an integer `n` as input. It first rotates the string `n` times by changing all the '0's to '1's and vice versa. Then it counts the number of '1's in the resulting string and returns this count. 

The unit test `assert odd_Equivalent("011001",6) == 3` checks the function with the given binary string "011001" and the number of rotations 6, and ensures that it returns the expected result 3. 

This function assumes that the input string `s` is a valid binary string, i.e., it only contains '0's and '1's. If the input string may contain other characters, the function should be modified to handle these cases. 





# Test the function

print(odd_Equivalent("011001",6)) # Expected output: 3
```


# Output
```
3
```
The function works correctly and returns the expected result.