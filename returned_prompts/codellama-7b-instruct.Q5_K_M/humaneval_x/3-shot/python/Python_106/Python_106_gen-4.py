    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def sum_numbers(n):
        result = 0
        for i in range(1, n + 1):
            result += i
        return result

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum_numbers(i))
    return result


