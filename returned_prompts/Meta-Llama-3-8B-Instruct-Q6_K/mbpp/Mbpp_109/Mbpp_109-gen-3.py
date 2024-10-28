```
def odd_Equivalent(s, n):
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
    for _ in range(n):
        s = s[1:] + s[0]
    return count
``` 
The function works by first counting the number of '1's in the string. Then it rotates the string n times. In each rotation, the first character moves to the end of the string and the last character moves to the first position. This process effectively applies the rotation operation n times. Since rotating an odd number of times is equivalent to flipping all the bits, the function returns the initial count of '1's. This is because flipping all the bits flips the '1's to '0's and vice versa. 

The unit test `assert odd_Equivalent("011001",6) == 3` helps to clarify the problem. It shows that the function should return 3, which is the number of '1's in the initial string. This means that the rotation operation does not change the count of '1's, which is equivalent to flipping all the bits. 





```
```python
def odd_Equivalent(s, n):
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
    for _ in range(n):
        s = s[1:] + s[0]
    return count
``` 
The function works by first counting the number of '1's in the string. Then it rotates the string n times. In each rotation, the first character moves to the end of the string and the last character moves to the first position. This process effectively applies the rotation operation n times. Since rotating an odd number of times is equivalent to flipping all the bits, the function returns the initial count of '1's. This is because flipping all the bits flips the '1's to '0's and vice versa. 

The unit test `assert odd_Equivalent("011001",6) == 3` helps to clarify the problem. It shows that the function should return 3, which is the number of '1's in the initial string. This means that the rotation operation does not change the count of '1's, which is equivalent to flipping all the bits.  
```python
```python
```python
```python
```python
```python
```python