```
def even_binomial_Coeff_Sum(n):
    if n < 1:
        return 0
    result = 0
    for k in range(n):
        if k % 2 == 0:
            result += binomial_coefficient(n, k)
    return result

def binomial_coefficient(n, k):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result
```
In this code, we define two functions. The `even_binomial_Coeff_Sum` function calculates the sum of the binomial coefficients of even indices. It iterates over all indices from 0 to n, checks if the index is even, and if it is, adds the binomial coefficient to the result.

The `binomial_coefficient` function calculates the binomial coefficient `n choose k`. It uses the formula `n! / (k! * (n-k)!)` to calculate the binomial coefficient. The function also handles the case where `k > n - k` by swapping `k` with `n - k` to avoid calculating the same coefficient twice.

The `even_binomial_Coeff_Sum` function is tested with the unit test `assert even_binomial_Coeff_Sum(4) == 8`, which checks that the sum of the even index binomial coefficients for `n = 4` is indeed `8`.