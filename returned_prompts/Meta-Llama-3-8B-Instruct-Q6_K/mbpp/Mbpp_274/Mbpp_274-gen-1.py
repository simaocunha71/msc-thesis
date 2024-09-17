The problem is asking to write a function that takes a positive integer n as input and returns the sum of all binomial coefficients at even indices. 

The binomial coefficient is calculated using the formula nCk = n! / (k!(n-k)!) where ! denotes the factorial function. 

The problem doesn't specify which binomial coefficients to sum, but based on the unit test `assert even_binomial_Coeff_Sum(4) == 8`, it seems that the sum is of all even index binomial coefficients.

Here is a python function that solves the problem:

```Python
import math

def even_binomial_Coeff_Sum(n):
    total = 0
    for k in range(n + 1):
        if k % 2 == 0:
            total += math.comb(n, k)
    return total
```

In this function, we iterate over all binomial coefficients from 0 to n. If the index k is even, we add the corresponding binomial coefficient to the total. The `math.comb(n, k)` function is used to calculate the binomial coefficient. The function returns the total sum of even index binomial coefficients. 

The unit test `assert even_binomial_Coeff_Sum(4) == 8` passes with this function. 

This function assumes that the input n is a positive integer. If the input can be negative or non-integer, additional error handling may be needed. 