"""
This function uses binomial coefficients to find the sum of even index binomial coefficients. It does this by using the formula for binomial coefficients (n k) = (n k) (n-k). It then sums up the binomial coefficients at even indices.
"""

def even_binomial_Coeff_Sum(n):
    even_sum = 0
    for k in range(0, n//2 + 1):
        even_sum += binomial_coefficient(n, k)
    return even_sum


def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


print(even_binomial_Coeff_Sum(4))  # 8
"""
This function first computes the binomial coefficient (n, k) using the recursive formula (n k) = (n k) (n-k). This is then stored in a list. The function then sums up the binomial coefficients at even indices.
"""


def even_binomial_Coeff_Sum(n):
    binomial_coeffs = [0] * (n + 1)
    binomial_coeffs[0] = 1
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            binomial_coeffs[j] += binomial_coeffs[j - 1]
    return sum(binomial_coeffs[i] for i in range(0, n + 1, 2))


print(even_binomial_Coeff_Sum(4))  # 8


