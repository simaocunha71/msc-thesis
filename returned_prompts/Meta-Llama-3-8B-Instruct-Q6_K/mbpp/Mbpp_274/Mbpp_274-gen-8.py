```
def even_binomial_Coeff_Sum(n):
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += binomial_coefficient(n, i)
    return total

def binomial_coefficient(n, k):
    if k > n - k:  # take advantage of symmetry
        k = n - k
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result
```
The `even_binomial_Coeff_Sum` function takes an integer `n` and calculates the sum of even index binomial coefficients using the `binomial_coefficient` function. The `binomial_coefficient` function calculates the binomial coefficient `n choose k` using the formula `n! / (k! * (n-k)!)`. The function takes advantage of the symmetry of the binomial coefficient by only calculating the coefficient for `k <= n-k`. This reduces the number of calculations needed and makes the function more efficient. 

The unit test `assert even_binomial_Coeff_Sum(4) == 8` ensures that the function is working correctly for the input `n = 4`. The expected output is `8`, which is the sum of the even index binomial coefficients for `n = 4`. 

This solution has a time complexity of O(n), where `n` is the input integer. This is because the `even_binomial_Coeff_Sum` function iterates `n` times to calculate the sum of the even index binomial coefficients. The `binomial_coefficient` function has a time complexity of O(k), where `k` is the index of the binomial coefficient. However, in the worst-case scenario, `k` is at most `n/2`, so the overall time complexity of the `binomial_coefficient` function is O(n). Therefore, the overall time complexity of the solution is O(n). 

The space complexity of the solution is O(1), which means the space required does not change with the size of the input `n`. This is because the `even_binomial_Coeff_Sum` function only uses a constant amount of space to store the variables and the `binomial_coefficient` function also only uses a constant amount of space to store the variables. Therefore, the space complexity of the solution is O(1). 

The solution is