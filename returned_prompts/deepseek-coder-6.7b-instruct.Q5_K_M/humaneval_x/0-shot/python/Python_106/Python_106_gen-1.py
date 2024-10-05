
def f(n):
    def factorial(i):
        if i == 0:
            return 1
        else:
            return i * factorial(i - 1)

    def summation(i):
        if i == 1:
            return 1
        else:
            return i + summation(i - 1)

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(summation(i))
    return result

print(f(5)) # [1, 2, 6, 24, 15]

