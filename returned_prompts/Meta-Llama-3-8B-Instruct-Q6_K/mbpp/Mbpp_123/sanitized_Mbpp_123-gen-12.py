def amicable_numbers_sum(n):
    def sum_divisors(num):
        return sum(i for i in range(1, num) if num % i == 0)

    def is_amicable(a, b):
        if a != b and sum_divisors(a) == b and sum_divisors(b) == a:
            return True
        return False

    total_sum = 0
    for i in range(1, n):
        for j in range(i, n):
            if is_amicable(i, j):
                total_sum += i + j
    return total_sum