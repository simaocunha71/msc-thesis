def f(n):
    def factorial(i):
        return 1 if i == 0 else i * factorial(i - 1)

    def sum_to_i(i):
        return sum(range(1, i + 1))

    return [factorial(i) if i % 2 == 0 else sum_to_i(i) for i in range(1, n + 1)]