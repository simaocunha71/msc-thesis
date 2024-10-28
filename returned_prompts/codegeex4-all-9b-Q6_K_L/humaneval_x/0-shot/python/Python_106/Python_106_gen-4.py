def f(n):
    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i + 1)))
    return result

print(f(5))  # Output: [1, 2, 6, 24, 15]