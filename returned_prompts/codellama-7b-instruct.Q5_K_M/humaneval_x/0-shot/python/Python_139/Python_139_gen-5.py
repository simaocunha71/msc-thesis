
def special_factorial(n):
    return n*special_factorial(n-1) if n>0 else 1
