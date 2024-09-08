
def even_binomial_Coeff_Sum(n):
    import math
    sum = 0
    for i in range(0, n//2+1):
        sum += math.comb(n, 2*i)
    return sum

print(even_binomial_Coeff_Sum(4)) # 8

Explanation:
The function `even_binomial_Coeff_Sum(n)` calculates the sum of binomial coefficients at even indices. 
This is done by iterating from 0 to `n//2`, and adding the binomial coefficient `C(n, 2*i)` for each `i`.
The binomial coefficient `C(n, k)` is the number of ways to choose `k` items from `n` items without repetition and without order.
The `math.comb(n, k)` function is used to calculate the binomial coefficient `C(n, k)`.
"""

# 2. Write a python function that takes in an integer n and finds the number of ways to express n as a sum of two squares.

