    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def sum_to_n(n):
        return n * (n + 1) // 2

    return [(factorial(i) if i % 2 == 0 else sum_to_n(i)) for i in range(1, n + 1)]


