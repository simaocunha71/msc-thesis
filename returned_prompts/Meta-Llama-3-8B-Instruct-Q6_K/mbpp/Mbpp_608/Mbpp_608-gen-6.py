The nth Bell number is the number of ways to partition a set of n elements, which is denoted by Bn. 

Here is a Python function that calculates the nth Bell number using dynamic programming:

```
def bell_Number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        B = [0]*(n+1)
        B[0] = 1
        B[1] = 1
        for i in range(2, n+1):
            B[i] = sum(binomial(i, k) * B[i-k] for k in range(i))
        return B[n]
```

This function uses the formula B(n) = Σ{k=0 to n} C(n, k) * B(n-k) to calculate the nth Bell number. The `binomial` function is used to calculate the binomial coefficient C(n, k).

The unit test `assert bell_Number(2) == 2` ensures that the function returns the correct result for n=2. 

This function assumes that the input n is a non-negative integer. If n is a negative integer or a non-integer, the function may not work correctly. You may want to add error handling to handle such cases.  """







