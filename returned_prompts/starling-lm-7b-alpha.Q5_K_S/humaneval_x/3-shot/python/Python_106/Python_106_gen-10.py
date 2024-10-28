    def f(n):
        result = [0] * n
        for i in range(n):
            if i % 2 == 0:
                result[i] = factorial(i)
            else:
                result[i] = sum_numbers(i)
        return result

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    def sum_numbers(n):
        if n == 1:
            return 1
        else:
            return n + sum_numbers(n - 1)

    return result


