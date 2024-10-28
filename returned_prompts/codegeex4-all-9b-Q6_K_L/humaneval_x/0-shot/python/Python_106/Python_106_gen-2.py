def f(n):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    def sum_of_numbers(n):
        return sum(range(1, n+1))

    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum_of_numbers(i))
    return result

print(f(5))