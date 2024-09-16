def amicable_numbers_sum(n):
    return sum([i for i in range(1, n+1) if sum_proper_divisors(i) == sum_proper_divisors(sum_proper_divisors(i))])
def sum_proper_divisors(n):
    return sum([i for i in range(1, int(n**0.5)+1) if n % i == 0])