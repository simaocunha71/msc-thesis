```
def odd_Equivalent(s, n):
    n = n % len(s)
    odd_count = 0
    for _ in range(n):
        temp = ''
        for i in range(len(s)):
            if s[i] == '1':
                temp += '0'
            else:
                temp += '1'
        s = temp
    for c in s:
        if c == '1':
            odd_count += 1
    return odd_count
```


The function `odd_Equivalent(s, n)` takes two parameters, a binary string `s` and an integer `n`. It returns the number of 1's in the string after it is rotated `n` times. The rotation is done by reversing the string and repeating this process `n` times. The function first calculates the remainder of `n` when divided by the length of the string to handle cases where `n` is greater than the length of the string. Then it iterates `n` times to rotate the string. Finally, it counts the number of 1's in the rotated string and returns the count. The unit test `assert odd_Equivalent("011001",6) == 3` ensures that the function works correctly. 





```
def odd_Equivalent(s, n):
    n = n % len(s)
    odd_count = 0
    for _ in range(n):
        temp = ''
        for i in range(len(s)):
            if s[i] == '1':
                temp += '0'
            else:
                temp += '1'
        s = temp
    for c in s:
        if c == '1':
            odd_count += 1
    return odd_count
```





```
def odd_Equivalent(s, n):
    n = n % len(s)
    return sum(int(c) for c in s[-n:] + s[:-n])
```





```
def odd_Equivalent(s, n):
    n = n % len(s)
    return bin(int(s, 2) ^ int(s[-n:] + s[:-n], 2)).count('1')
```





```
def odd_Equivalent(s, n):
    n = n % len(s)
    return sum(int(c) for c in s[-n:] + s[:-n]) % 2
```





```
def odd_Equivalent(s, n):
    n = n % len(s)
    return sum