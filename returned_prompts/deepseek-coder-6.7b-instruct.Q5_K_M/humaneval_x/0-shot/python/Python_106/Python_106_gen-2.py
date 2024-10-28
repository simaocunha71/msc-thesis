
def f(n):
    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    def summation(x):
        return (x * (x + 1)) // 2

    return [factorial(i) if i % 2 == 0 else summation(i) for i in range(1, n+1)]

print(f(5))  # [1, 2, 6, 24, 15]

# Solution 2

def f(n):
    def factorial(x):
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    def summation(x):
        return (x * (x + 1)) // 2

    return [factorial(i) if i % 2 == 0 else summation(i) for i in range(1, n+1)]

print(f(5))  # [1, 2, 6, 24, 15]

# Solution 3

def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            j = 2
            factorial = 1
            while j <= i:
                factorial *= j
                j += 1
            result.append(factorial)
        else:
            result.append(int(i * (i + 1) / 2))
    return result

print(f(5))  # [1, 2, 6, 24, 15]

# Solution 4

def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            result.append(factorial)
        else:
            result.append(int((i * (i + 1)) / 2))
    return result

print(f(5))  # [1