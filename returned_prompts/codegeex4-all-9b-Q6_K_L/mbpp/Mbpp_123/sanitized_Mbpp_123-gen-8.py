def amicable_numbers_sum(n):
    def sum_of_divisors(x):
        sum = 1
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                sum += i
                if i != x // i:
                    sum += x // i
        return sum

    amicable_sum = 0
    for i in range(2, n + 1):
        j = sum_of_divisors(i)
        if j != i and sum_of_divisors(j) == i:
            amicable_sum += i + j

    return amicable_sum // 2