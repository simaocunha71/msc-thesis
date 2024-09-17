```
def even_binomial_Coeff_Sum(n):
    sum_even_index_binomial_coeff = 0
    for i in range(n):
        for j in range(i + 1):
            if (i - j) % 2 == 0:
                sum_even_index_binomial_coeff += binomial(i, j)
    return sum_even_index_binomial_coeff
```
The `binomial` function is not built-in in python, so you need to define it yourself or use the `math.comb` function from python 3.8 onwards.

For example:
```
import math

def even_binomial_Coeff_Sum(n):
    sum_even_index_binomial_coeff = 0
    for i in range(n):
        for j in range(i + 1):
            if (i - j) % 2 == 0:
                sum_even_index_binomial_coeff += math.comb(i, j)
    return sum_even_index_binomial_coeff
```
This function works by iterating over all the binomial coefficients of `n`, and adding the ones that are at an even index to the sum. The `binomial` function calculates the binomial coefficient `n choose k`, which is defined as `n! / (k! * (n-k)!)`. The `math.comb` function in python 3.8 onwards calculates the binomial coefficient directly. 

The unit test `assert even_binomial_Coeff_Sum(4) == 8` checks that the function returns the correct sum for `n = 4`. 

Please note that the problem is not clearly defined and the unit test suggests that the problem is asking for the sum of even index binomial coefficients in the expansion of `(1 + x)^n`. If this is not the case, the problem should be rephrased. 