```
def sum_Of_product(n):
    sum = 0
    for i in range(1, n+1):
        binomial_coefficient = 1
        for j in range(1, i+1):
            binomial_coefficient *= (n-j+1) / j
        sum += binomial_coefficient
    return sum
```


Explanation:
The function `sum_Of_product(n)` calculates the sum of the product of consecutive binomial coefficients. 
The binomial coefficient is calculated using the formula `n choose k = n! / (k! * (n-k)!)`. 
The function uses nested loops to calculate the binomial coefficients and their products, and then sums them up. 
The unit test `assert sum_Of_product(3) == 15` checks if the function correctly calculates the sum of the product of consecutive binomial coefficients for `n=3`. 

This function is not efficient for large values of `n` because it calculates the binomial coefficients and their products from scratch. 
For large values of `n`, a more efficient approach would be to use the property of binomial coefficients that `C(n, k) = C(n-1, k-1) * (n-k+1) / k` to avoid redundant calculations. 
However, this problem is designed to be solved using the given formula, and the function should work correctly for small values of `n`. 
For larger values of `n`, a more efficient solution would be needed. 





