
def f(n):
    return [sum(range(1, i+1)) if i % 2 else i * factorial(i) for i in range(1, n+1)]

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
