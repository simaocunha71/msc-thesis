from math import factorial
def bell_number(n):
    if n == 0:
        return 1
    else:
        return sum(factorial(n) / (factorial(k) * factorial(n - k)) for k in range(n + 1))