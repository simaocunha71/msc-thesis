def amicable_numbers_sum(n):
    def sum_proper_divisors(x):
        sum = 1
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                if i == x / i:
                    sum += i
                else:
                    sum += i + x / i
        return sum

    result = 0
    for i in range(1, n + 1):
        if i == sum_proper_divisors(sum_proper_divisors(i)) and i != sum_proper_divisors(i):
            result += i
    return result