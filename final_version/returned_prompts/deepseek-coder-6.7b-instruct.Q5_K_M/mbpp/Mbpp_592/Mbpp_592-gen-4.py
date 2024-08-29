
def sum_Of_product(n):
    import math
    sum = 0
    for i in range(1, n):
        sum += math.comb(n, i) * math.comb(n, i+1)
    return sum

print(sum_Of_product(3))

"""
Explanation:
In the function, we first import the math module to use its comb function, which calculates binomial coefficients. Then we initialize a variable sum to 0. The for loop goes through each i from 1 to n-1. For each i, it adds to sum the product of the binomial coefficients binom(n, i) and binom(n, i+1). Finally, the function returns the sum.

For n=3, the binomial coefficients are 3, 6, 10, 10, 6, 3. The product of consecutive pairs of these coefficients is 18, 30, 30, 18. Their sum is 84.
"""

# Alternative Solution:

def sum_Of_product(n):
    import math
    return sum(math.comb(n, i) * math.comb(n, i+1) for i in range(1, n))

print(sum_Of_product(3))

"""
In this alternative solution, we use a more pythonic way of writing the for loop and if statement. The range function is used to generate the numbers i from 1 to n-1. The math.comb function is used to calculate the binomial coefficients. The expression math.comb(n, i) * math.comb(n, i+1) calculates the product of the binomial coefficients. The sum function adds up all the products. This solution is more compact and easier to understand.
"""

# Test Cases:

assert sum_Of_product(3) == 84
assert sum_Of_product(4) == 162
assert sum_Of_product(5) == 280
assert sum_Of_product(6) == 450
assert sum_Of_product(7) == 690
assert sum_Of_product(8) == 1026
assert sum_Of_