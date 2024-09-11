"""
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
"""

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

assert amicable_numbers_sum(999)==504

#def amicable_numbers_sum(n):
#    return sum(set(i for i in range(1,n+1) if i != sum_of_proper_divisors(i) and sum_of_proper_divisors(sum_of_proper_divisors(i)) == i))

```
This code defines a function `amicable_numbers_sum` that returns the sum of all amicable numbers from 1 to the input number `n`. The function `sum_of_proper_divisors` is used to calculate the sum of the proper divisors of a number. An amicable number is a number that is equal to the sum of its proper divisors, excluding the number itself. The function `amicable_numbers_sum` iterates through the range from 1 to `n`, checks if the number