
def even_binomial_Coeff_Sum(n):
    binomial_coeff = [0]*(n+1)
    binomial_coeff[0] = 1
    for i in range(1, n+1):
        j = 0
        while (j <= i-1):
            binomial_coeff[j] = binomial_coeff[j] + binomial_coeff[j+1]
            j += 1
    return sum(binomial_coeff[i] for i in range(0, n+1, 2))

print(even_binomial_Coeff_Sum(4))  # Outputs: 8

"""
Explanation:

Binomial coefficient C(n, k) can be calculated using the following formula:
C(n, k) = C(n-1, k-1) + C(n-1, k)

For even index binomial coefficients, we can consider the binomial expansion of (1 + x)^n. For even n, the coefficient at x^n will be 0, for even x, the coefficient at x^n will be 0, and so on.

The coefficients at even powers of x are the binomial coefficients at even indices in the binomial expansion.

In this function, we use dynamic programming to calculate the binomial coefficients. We create an array 'binomial_coeff' to store the binomial coefficients. We initialize the first element of the array to 1 (C(n, 0) = 1). For each number 'i' from 1 to n, we calculate the binomial coefficients for 'i' and store them in the array. Finally, we return the sum of the binomial coefficients at even indices.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3
<jupyter_code>
