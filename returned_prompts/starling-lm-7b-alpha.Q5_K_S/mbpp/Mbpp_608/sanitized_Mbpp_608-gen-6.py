from math import factorial
def bell_Number(n):
    if n == 0:
        return 1
    else:
        return factorial(2*n)/(factorial(n+1)*factorial(n))