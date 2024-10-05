def special_factorial(n):
    if n == 0:
        return 1
    else:
        return n * special_factorial(n-1) * special_factorial(n-2)
special_factorial(4)