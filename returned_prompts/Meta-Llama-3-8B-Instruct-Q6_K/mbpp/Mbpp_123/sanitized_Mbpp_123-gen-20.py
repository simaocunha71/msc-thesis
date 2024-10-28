def amicable_numbers_sum(n):
    def sum_factors(num):
        factors = set()
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                factors.add(i)
                if i != num // i:
                    factors.add(num // i)
        return sum(factors) - num

    amicable_sum = 0
    for i in range(1, n + 1):
        if i == sum_factors(sum_factors(i)):
            amicable_sum += i
    return amicable_sum