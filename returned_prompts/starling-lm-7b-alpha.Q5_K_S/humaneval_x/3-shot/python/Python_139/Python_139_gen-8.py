    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return factorial(n) * factorial(n-1) * factorial(n-2)


