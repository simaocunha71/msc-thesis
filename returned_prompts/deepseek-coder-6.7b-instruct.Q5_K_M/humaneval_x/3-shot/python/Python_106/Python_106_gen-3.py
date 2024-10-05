    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    def sum_up_to_n(n):
        return n * (n + 1) // 2

    return [factorial(i) if i % 2 == 0 else sum_up_to_n(i) for i in range(1, n+1)]


