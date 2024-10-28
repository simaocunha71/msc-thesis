def sum_divisors(n):
    i = 1
    sum = 0
    while i <= n:
        if n % i == 0:
            sum += i
        i += 1
    return sum
def amicable_numbers_sum(n):
    sum = 0
    for i in range(1, n+1):
        div_sum = sum_divisors(i)
        if i != div_sum and sum_divisors(div_sum) == i:
            sum += i
    return sum