def amicable_numbers_sum(n):
    def divisor_sum(x):
        total = 0
        for i in range(1, x):
            if x % i == 0:
                total += i
        return total

    total = 0
    for i in range(1, n + 1):
        j = divisor_sum(i)
        if j != i and divisor_sum(j) == i:
            total += i
    return total