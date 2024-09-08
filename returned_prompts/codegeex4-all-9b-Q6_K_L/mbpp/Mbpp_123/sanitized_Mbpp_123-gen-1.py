def amicable_numbers_sum(n):
    def sum_of_divisors(x):
        total = 1
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                total += i
                if i != x // i:
                    total += x // i
        return total

    return sum(x for x in range(2, n + 1) if sum_of_divisors(x) == sum_of_divisors(sum_of_divisors(x)) and sum_of_divisors(x) != x)