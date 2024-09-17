def amicable_numbers_sum(n):
    total = 0
    for i in range(1,n+1):
        if i != sum_of_proper_divisors(i):
            if sum_of_proper_divisors(sum_of_proper_divisors(i)) == i:
                total += i
    return total
def sum_of_proper_divisors(n):
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            sum += i
    return sum