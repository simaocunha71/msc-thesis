def f(n):
    from math import factorial

    def factorial_sum(n):
        if n == 1:
            return 1
        else:
            return n + factorial_sum(n - 1)

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(factorial_sum(i))
    return result

print(f(5))