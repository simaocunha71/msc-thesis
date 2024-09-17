def amicable_numbers_sum(n):
    amicable_nums = []
    for i in range(1, n+1):
        if i == sum(divisors(i))-i:
            amicable_nums.append(i)
    return sum(amicable_nums)
def divisors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))