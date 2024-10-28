def amicable_numbers_sum(n):
    def sum_of_divisors(num):
        sum_divisors = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum_divisors += i
                if i != num // i:
                    sum_divisors += num // i
        return sum_divisors

    amicable_sum = 0
    for i in range(2, n + 1):
        j = sum_of_divisors(i)
        if sum_of_divisors(j) == i and i != j:
            amicable_sum += i
    return amicable_sum