
def f(n):
    result = [0] * n
    for i in range(n):
        if i % 2 == 0:
            result[i] = factorial(i)
        else:
            result[i] = sum(range(1, i + 1))
    return result

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
