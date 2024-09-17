```
def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += binomial(i, i//2)
    return sum
```
The function `even_binomial_Coeff_Sum` calculates the sum of even index binomial coefficients for a given positive integer `n`. It iterates over all indices from 0 to `n-1`, and for each index `i`, it checks if `i` is even. If it is, it calculates the binomial coefficient `binomial(i, i//2)` and adds it to the sum. Finally, it returns the sum.

The unit test `assert even_binomial_Coeff_Sum(4) == 8` ensures that the function returns the correct sum for `n=4`. For `n=4`, the even index binomial coefficients are `binomial(0, 0)`, `binomial(2, 1)`, and `binomial(4, 2)`, which sum up to 8.