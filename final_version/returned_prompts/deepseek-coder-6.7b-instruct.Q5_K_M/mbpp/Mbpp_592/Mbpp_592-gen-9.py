"""
The function sum_Of_product(n) uses a loop to calculate the binomial co-efficients and their products. The sum of the products is then returned.

In the given example, the binomial co-efficients are calculated as:
    (3 choose 0) * (3 choose 1) = 1 * 3 = 3
    (3 choose 1) * (3 choose 2) = 3 * 3 = 9
    (3 choose 2) * (3 choose 3) = 3 * 1 = 3

And the sum of the products is 3 + 9 + 3 = 15.
"""

def sum_Of_product(n):
    import math
    sum_of_product = 0
    for i in range(n+1):
        sum_of_product += math.comb(n, i) * math.comb(n, i+1)
    return sum_of_product

print(sum_Of_product(3))
assert sum_Of_product(3) == 15

# Using math.comb() in Python 3.8 or above is required. If you're using an earlier version of Python, you would need to use math.factorial() to calculate the binomial co-efficients.
def sum_Of_product(n):
    import math
    sum_of_product = 0
    for i in range(n+1):
        sum_of_product += math.factorial(n) // (math.factorial(i) * math.factorial(n-i)) * math.factorial(n) // (math.factorial(i+1) * math.factorial(n-i-1))
    return sum_of_product

print(sum_Of_product(3))
assert sum_Of_product(3) == 15
<jupyter_output>
15
15
<jupyter_text>
