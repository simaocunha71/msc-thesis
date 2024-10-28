from math import factorial
def sum_Of_product(n):
    return sum([factorial(n-i)//(factorial(i)*factorial(n-2*i)) for i in range(n//2+1)])