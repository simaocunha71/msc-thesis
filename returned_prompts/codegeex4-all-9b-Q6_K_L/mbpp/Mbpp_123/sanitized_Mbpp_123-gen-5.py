def amicable_numbers_sum(n):
    def proper_divisors_sum(x):
        sum = 1
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                sum += i
                if i != x // i:
                    sum += x // i
        return sum

    amicable_numbers = []
    for i in range(2, n + 1):
        j = proper_divisors_sum(i)
        if j != i and proper_divisors_sum(j) == i:
            amicable_numbers.append(i)

    return sum(amicable_numbers)