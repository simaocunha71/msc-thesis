
def amicable_numbers_sum(n):
    def sum_divisors(num):
        sum = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i:
                continue
            elif i * i != num:
                sum = sum + i + num // i
            else:
                sum = sum + i
        return sum

    amicable_nums_sum = 0
    for i in range(1, n + 1):
        if i == sum_divisors(sum_divisors(i)) and i != sum_divisors(i):
            amicable_nums_sum += i
    return amicable_nums_sum


