    def factorial(n: int) -> int:
        """ Calculate factorial of a number """
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    result = [0] * n
    for i in range(n):
        if i % 2 == 0:
            result[i] = factorial(i)
        else:
            result[i] = i * (i+1) // 2

    return result


