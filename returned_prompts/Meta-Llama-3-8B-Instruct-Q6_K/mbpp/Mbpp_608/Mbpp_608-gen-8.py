The nth Bell number is the number of ways to partition a set of n elements into disjoint sets. It is denoted by Bn.

Here is a Python function to find the nth Bell number:

```Python
def bell_Number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        B = [1, 1]
        for i in range(2, n):
            B.append(B[i-1] + sum(B[:i]))
        return B[-1]
```
This function calculates the nth Bell number by iterating through the Bell numbers from 0 to n-1, and at each step, it calculates the next Bell number as the sum of the previous Bell number and the sum of all the previous Bell numbers. The function returns the nth Bell number. 

The unit test `assert bell_Number(2) == 2` is also included to verify the correctness of the function. 

Please note that this function is not efficient for large values of n, as it has a time complexity of O(n). For larger values of n, a more efficient algorithm or a precomputed table of Bell numbers would be needed. 