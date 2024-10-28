def amicable_numbers_sum(n):
    def sum_divisors(num):
        return sum([i for i in range(1, num) if num % i == 0])

    amicable_sums = []
    for i in range(2, n + 1):
        j = sum_divisors(i)
        if sum_divisors(j) == i and i != j:
            amicable_sums.append(i)

    return sum(amicable_sums)