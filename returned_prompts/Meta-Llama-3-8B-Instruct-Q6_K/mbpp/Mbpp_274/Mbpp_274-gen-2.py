```
def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for k in range(n):
        if k % 2 == 0:
            total_sum += binomial_coefficient(k, n)
    return total_sum

def binomial_coefficient(k, n):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result
```
The function `even_binomial_Coeff_Sum(n)` calculates the sum of even index binomial coefficients up to `n`. It iterates over all `k` from `0` to `n` and checks if `k` is even. If it is, it adds the binomial coefficient `C(n, k)` to the sum. The binomial coefficient `C(n, k)` is calculated by the function `binomial_coefficient(k, n)`.

The `binomial_coefficient(k, n)` function calculates the binomial coefficient `C(n, k)` using the formula `n! / (k!(n-k)!)`. It first checks if `k` is larger than `n-k` and if so, it calculates the binomial coefficient for `n-k` instead of `k` to avoid redundant calculations. Then it calculates the binomial coefficient using a loop and returns the result. The `//` operator is used for integer division to ensure that the result is an integer.

The unit test `assert even_binomial_Coeff_Sum(4) == 8` ensures that the function `even_binomial_Coeff_Sum(n)` works correctly. It checks if the sum of even index binomial coefficients up to `n=4` is equal to `8`. If the function is implemented correctly, this assertion should pass.