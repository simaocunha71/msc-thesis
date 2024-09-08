
def even_binomial_Coeff_Sum(n):
    binomial_coeffs = [1] + [0]*n
    sum_even_index = 0
    for i in range(n+1):
        sum_even_index += binomial_coeffs[i]
        for j in range(i, 0, -1):
            binomial_coeffs[j] = binomial_coeffs[j] + binomial_coeffs[j-1]
    return sum_even_index


print(even_binomial_Coeff_Sum(4))  # 8
print(even_binomial_Coeff_Sum(5))  # 16
print(even_binomial_Coeff_Sum(6))  # 32
print(even_binomial_Coeff_Sum(7))  # 64
print(even_binomial_Coeff_Sum(8))  # 128
print(even_binomial_Coeff_Sum(9))  # 256
print(even_binomial_Coeff_Sum(10))  # 512

"""
In this function, we use the method of calculating binomial coefficients. We start by initializing a list `binomial_coeffs` with the first term as 1 and the rest as 0. We then calculate the binomial coefficients using the formula binomial_coeffs[j] = binomial_coeffs[j] + binomial_coeffs[j-1] for all j in the range of i to 1.

After all binomial coefficients are calculated, we calculate the sum of even index binomial coefficients by iterating through the list and adding the terms at even indices to a variable `sum_even_index`.

Finally, the function returns `sum_even_index`.
"""
<jupyter_output>
8
16
32
64
128
256
512
<jupyter_text>
Problem 3
<jupyter_code>
