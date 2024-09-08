def proper_divisors_sum(n):
    divisors_sum = 0
    for i in range(1,n):
        if n%i == 0:
            divisors_sum += i
    return divisors_sum
def amicable_numbers_sum(n):
    amicable_numbers_sum = 0
    for i in range(1,n):
        if proper_divisors_sum(proper_divisors_sum(i)) == i and proper_divisors_sum(i) != i:
            amicable_numbers_sum += i
    return amicable_numbers_sum