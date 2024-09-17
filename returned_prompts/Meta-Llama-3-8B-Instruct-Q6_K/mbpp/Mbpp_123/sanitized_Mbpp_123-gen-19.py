def amicable_numbers_sum(n):
    def sum_of_proper_divisors(num):
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors

    total = 0
    for i in range(1, n+1):
        num1 = sum_of_proper_divisors(i)
        if num1 > i and sum_of_proper_divisors(num1) == i:
            total += i + num1
    return total