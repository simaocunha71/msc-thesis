
def f(n):
    return [sum(range(1, i+1)) if i%2 else math.factorial(i) for i in range(1, n+1)]
