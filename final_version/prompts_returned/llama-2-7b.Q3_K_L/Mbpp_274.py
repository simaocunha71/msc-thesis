"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""

def even_binomial_Coeff_Sum(n):
    bin = [[]]
    for i in range(1, n+1):
        bin = [j for j in bin if i%j==0]
    
    sum = 0
    for x in bin:
        sum += 1/2**(len(x)+1)
    return sum