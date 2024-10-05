    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)

    def summation(n):
        return n * (n + 1) // 2

    return [factorial(i) if i % 2 == 0 else summation(i) for i in range(1, n+1)]


