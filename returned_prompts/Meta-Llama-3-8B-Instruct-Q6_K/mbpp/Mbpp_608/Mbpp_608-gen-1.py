The Bell numbers are a sequence of numbers that count the number of ways to partition a set of size n. Here is the python function to find the nth Bell number:

```python
def bell_Number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return sum(bell_Number(i) * bell_Number(n - i - 1) for i in range(n))
```
This function uses recursion to calculate the nth Bell number. The base cases are when n is 0 or 1, in which case the function returns 1. For n greater than 1, the function calculates the sum of the product of the ith Bell number and the (n-i-1)th Bell number for all i in the range from 0 to n-1. 

The unit test `assert bell_Number(2) == 2` ensures that the function returns the correct result for the second Bell number, which is 2. 

Please note that this function can be slow for large values of n, because it needs to calculate many Bell numbers. For large values of n, a more efficient algorithm would be needed.  A closed-form expression for the Bell numbers is not known, but there are many approximations and recursive formulas that can be used to calculate them.  One such formula is the following:

B_n = sum(C(n, k) * B_k for k in range(n))

where C(n, k) is the binomial coefficient. This formula can be used to calculate the Bell numbers iteratively, which is more efficient than the recursive formula used in the above function. 

Here is an example of how you could use this formula to calculate the Bell numbers iteratively:

```python
def bell_Number(n):
    if n == 0:
        return 1
    else:
        B = [0] * (n + 1)
        B[0] = 1
        for k in range(n):
            for i in range(k + 1, n + 1):
                B[i] += C(i, k) * B[k]
        return B[n]
```

This function initializes an array B of size n + 1 with all elements set to 0, except for B[0], which is set to 1. It then iterates over the range from 0 to n, and for each k, it calculates the (k + 1)th Bell number as