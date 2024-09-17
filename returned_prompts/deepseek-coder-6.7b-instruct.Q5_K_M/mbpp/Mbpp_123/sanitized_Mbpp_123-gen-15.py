def sum_of_factors(n):
    sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum
def amicable_numbers_sum(limit):
    result = 0
    for i in range(2, limit + 1):
        sum1 = sum_of_factors(i)
        if (sum1 > i and sum_of_factors(sum1) == i):
            result += i
    return result