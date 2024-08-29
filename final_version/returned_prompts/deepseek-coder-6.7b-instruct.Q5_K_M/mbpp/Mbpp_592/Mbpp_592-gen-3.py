
def sum_Of_product(n):
    import math
    sum_val = 0
    for i in range(n):
        sum_val += math.comb(n, i) * math.comb(n, i + 1)
    return sum_val

print(sum_Of_product(3))

"""
Explanation:

Here, we are using the concept of binomial coefficient. It is used in combinatorics to count the number of ways to choose a subset of a certain size from a total set.

The sum of the product of consecutive binomial coefficients can be obtained by iterating from 0 to n and taking the product of binomial coefficients at position i and i+1.

The function `math.comb(n, k)` is used to calculate binomial coefficient.
"""
<jupyter_output>
15
<jupyter_text>
Question 2
<jupyter_code>
"""
