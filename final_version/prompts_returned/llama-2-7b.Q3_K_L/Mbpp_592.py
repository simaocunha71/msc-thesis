"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""
from math import factorial, comb
def sum_of_product(N): # 3 is the length of the subarray
    ans=0
    for i in range (1, N+1):
        ans += comb(i, i-1)*factorial(i)**2
    return ans