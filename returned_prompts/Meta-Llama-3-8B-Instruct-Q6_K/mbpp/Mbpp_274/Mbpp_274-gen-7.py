```
def even_binomial_Coeff_Sum(n):
    result = 0
    for i in range(0, n):
        if i % 2 == 0:
            result += binomial_coefficient(n, i)
    return result

def binomial_coefficient(n, k):
    if k > n - k:  # take advantage of symmetry
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result
```
Explanation:
The function `even_binomial_Coeff_Sum` calculates the sum of even index binomial coefficients. It does this by iterating over the range from 0 to n (inclusive) and checking if the current index is even. If it is, it adds the binomial coefficient at that index to the result. The binomial coefficient is calculated using the function `binomial_coefficient`.

The `binomial_coefficient` function calculates the binomial coefficient `n choose k` using the formula `n! / (k! * (n-k)!)`. It takes advantage of the symmetry of the binomial coefficient to avoid calculating the same value twice. This is done by checking if `k` is greater than `n-k`, and if so, setting `k` to `n-k`. This allows the function to calculate the binomial coefficient in a more efficient way.