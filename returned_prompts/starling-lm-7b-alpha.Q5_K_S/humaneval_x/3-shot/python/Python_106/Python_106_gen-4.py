    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    def sum_numbers(n):
        if n == 1:
            return 1
        else:
            return n + sum_numbers(n-1)

    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum_numbers(i))
    return result


