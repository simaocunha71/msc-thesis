def sum_proper_divisors(n):
    sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i:
            continue
        if i * i != n:
            sum = sum + i + n // i
        else:
            sum = sum + i
    return sum
def amicable_numbers_sum(limit):
    sum_div = [0] * (limit + 1)
    for i in range(1, limit + 1):
        sum_div[i] = sum_proper_divisors(i)
    sum_amicable = 0
    for i in range(1, limit + 1):
        if sum_div[i] <= limit and sum_div[sum_div[i]] == i and i != sum_div[i]:
            sum_amicable += i
    return sum_amicable