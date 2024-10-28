    def factorial(n: int):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    return factorial(n) * factorial(n-1) * factorial(n-2) * ... * factorial(1)


