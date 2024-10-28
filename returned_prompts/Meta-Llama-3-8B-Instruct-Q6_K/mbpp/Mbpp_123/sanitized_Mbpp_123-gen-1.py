def amicable_numbers_sum(n):
    def sum_of_divisors(num):
        sum_div = 0
        for i in range(1, int(num/2) + 1):
            if num % i == 0:
                sum_div += i
        return sum_div

    total_sum = 0
    for i in range(1, n+1):
        if sum_of_divisors(i) > i:
            j = sum_of_divisors(i)
            if j > i and sum_of_divisors(j) == i:
                total_sum += i + j - i
    return total_sum