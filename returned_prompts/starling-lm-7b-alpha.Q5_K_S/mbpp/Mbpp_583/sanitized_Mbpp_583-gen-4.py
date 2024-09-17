def catalan_number(n):
    factorial = lambda x: reduce(lambda y: y * x, range(2, x + 1), 1)
    return factorial(2 * n) / (factorial(n + 1) * factorial(n))