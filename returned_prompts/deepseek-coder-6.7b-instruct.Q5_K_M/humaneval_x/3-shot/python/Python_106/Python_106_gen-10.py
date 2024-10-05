    def factorial(x):
        if x == 1 or x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    def summation(x):
        return x * (x + 1) // 2

    return [factorial(i) if i % 2 == 0 else summation(i) for i in range(1, n + 1)]


