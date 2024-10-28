def amicable_numbers_sum(n):
    def sum_factors(x):
        return sum(i for i in range(1, x) if x % i == 0)

    def is_amicable(x):
        return sum_factors(sum_factors(x)) == x and x != sum_factors(x)

    return sum(i for i in range(1, n+1) if is_amicable(i))