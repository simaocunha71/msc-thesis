    def factorial(i):
        result = 1
        for j in range(1, i + 1):
            result *= j
        return result

    def sum_up_to_i(i):
        return i * (i + 1) // 2

    return [(factorial(i) if i % 2 == 0 else sum_up_to_i(i)) for i in range(1, n + 1)]


