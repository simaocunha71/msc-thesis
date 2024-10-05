    def factorial(i):
        if i == 0:
            return 1
        else:
            return i * factorial(i - 1)

    def sum_numbers(i):
        if i == 1:
            return 1
        else:
            return i + sum_numbers(i - 1)

    return [factorial(i) if i % 2 == 0 else sum_numbers(i) for i in range(1, n + 1)]


