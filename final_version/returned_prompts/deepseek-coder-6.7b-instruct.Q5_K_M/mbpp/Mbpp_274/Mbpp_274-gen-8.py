
def even_binomial_Coeff_Sum(n):
    def binomial_coeff(n, k):
        res = 1
        if (k > n - k):
            k = n - k
        for i in range(0 , k):
            res = res * (n - i)
            res = res // (i + 1)
        return res

    sum = 0
    for i in range(0, n + 1, 2):
        sum += binomial_coeff(n, i)

    return sum

print(even_binomial_Coeff_Sum(4)) # 8


"""
Here, the binomial_coeff function is used to calculate binomial coefficients. The even_binomial_coeff_sum function sums up the binomial coefficients at even indices. It does this by using a for loop to iterate over even indices from 0 to n, inclusive. For each index i, it calculates the binomial coefficient C(n, i) and adds it to the sum. Finally, it returns the sum.
"""
<jupyter_output>
8
<jupyter_text>
Question 3
<jupyter_code>
