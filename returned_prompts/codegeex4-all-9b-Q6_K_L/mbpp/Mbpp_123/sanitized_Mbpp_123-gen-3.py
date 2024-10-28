def amicable_numbers_sum(n):
    def sum_of_divisors(x):
        sum_divisors = 1
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                sum_divisors += i
                if i != x // i:
                    sum_divisors += x // i
        return sum_divisors

    amicable_sum = 0
    for i in range(2, n + 1):
        if i == sum_of_divisors(sum_of_divisors(i)) and i != sum_of_divisors(i):
            amicable_sum += i

    return amicable_sum