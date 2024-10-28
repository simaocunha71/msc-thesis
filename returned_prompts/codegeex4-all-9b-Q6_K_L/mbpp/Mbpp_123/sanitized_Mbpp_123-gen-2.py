def amicable_numbers_sum(n):
    def sum_of_divisors(x):
        return sum(i for i in range(1, x) if x % i == 0)

    amicable_sum = 0
    for i in range(2, n + 1):
        j = sum_of_divisors(i)
        if sum_of_divisors(j) == i and i != j:
            amicable_sum += i + j

    return amicable_sum