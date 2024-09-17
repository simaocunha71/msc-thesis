def eulerian_num(n, m):
    return (factorial(n) / (factorial(m) * factorial(n - m)))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)