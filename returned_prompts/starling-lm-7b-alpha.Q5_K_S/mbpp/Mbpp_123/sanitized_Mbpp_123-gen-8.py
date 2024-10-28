def amicable_numbers_sum(n):
    amicable_numbers = set()
    for i in range(1, n + 1):
        if i == sum(divisors(i)) - i:
            amicable_numbers.add(i)
    return sum(amicable_numbers)
def divisors(n):
    divisors = set()
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)