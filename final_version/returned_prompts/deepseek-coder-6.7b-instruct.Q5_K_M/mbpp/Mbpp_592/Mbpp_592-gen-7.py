
def sum_Of_product(n):
    import math
    sum = 0
    for i in range(n-1):
        sum += math.comb(n, i) * math.comb(n, i+1)
    return sum

print(sum_Of_product(3))


Explanation:

In the function, we iterate from 0 to n-2 (as we are calculating the product of consecutive binomial coefficients). For each iteration, we calculate the product of the binomial coefficients at i and i+1 and add it to the sum.

The binomial coefficients are calculated using the comb function from the math module. The comb(n, i) function returns the number of ways to choose i items from n items without repetition and without order.
"""

# Solution 2:

"""
