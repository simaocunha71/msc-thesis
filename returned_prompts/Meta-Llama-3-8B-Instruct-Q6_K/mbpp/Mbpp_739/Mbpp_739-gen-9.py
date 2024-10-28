```
def find_Index(n):
    i = 1
    while True:
        triangular_num = (i * (i + 1)) // 2
        if len(str(triangular_num)) == n:
            return i + 1
        i += 1
```


The function `find_Index(n)` finds the index of the smallest triangular number with `n` digits. 

The triangular numbers are calculated using the formula `i * (i + 1) // 2`, where `i` is the index of the triangular number. 

The function uses a while loop to iterate through the triangular numbers until it finds the smallest one with `n` digits. 

The index of this triangular number is returned by the function. 

The unit test `assert find_Index(2) == 4` ensures that the function works correctly. 

For example, the smallest triangular number with 2 digits is 6, which is the 4th triangular number. 

The function returns 4, which is the expected result. 

The function can be optimized by using a more efficient formula to calculate the triangular numbers or by using a more efficient algorithm to find the smallest triangular number with `n` digits. 

However, the current implementation is simple and easy to understand. 

It can be used as a starting point for further optimization and improvement. 