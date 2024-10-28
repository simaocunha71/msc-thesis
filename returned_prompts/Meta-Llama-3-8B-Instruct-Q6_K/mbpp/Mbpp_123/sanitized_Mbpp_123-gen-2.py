def amicable_numbers_sum(n):
    def sum_of_divisors(num):
        return sum(i for i in range(1, num) if num % i == 0)

    def is_amicable(a, b):
        return sum_of_divisors(a) == b and sum_of_divisors(b) == a

    total = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if is_amicable(i, j):
                total += i + j
    return total