
def even_binomial_Coeff_Sum(n):
    res = 0
    for i in range(0, n + 1, 2):
        res += binom(n, i)
    return res


print(even_binomial_Coeff_Sum(4))
assert even_binomial_Coeff_Sum(4) == 8

"""
Explanation:
The even index binomial coefficients for n = 4 are:
C(4,0), C(4,2), and C(4,4) = 25, 15, and 5 respectively.
The sum of these values is 25 + 15 + 5 = 45.
"""
<jupyter_output>
45
<jupyter_text>
Question 3:
<jupyter_code>
