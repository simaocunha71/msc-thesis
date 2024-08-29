def sum_proper_divisors(n): 
    sum = 1 
    for i in range(2, int(n**0.5) + 1): 
        if n % i: 
            continue
        if i == n // i: 
            sum += i 
        else: 
            sum += i + n // i 
    return sum 

def amicable_numbers_sum(limit): 
    amicable_numbers_sum = 0 
    checked_numbers = [False] * (limit + 1) 
    for i in range(1, limit + 1): 
        if checked_numbers[i]: 
            continue 
        sum_i = sum_proper_divisors(i) 
        if sum_i <= limit and sum_i != i and sum_proper_divisors(sum_i) == i: 
            amicable_numbers_sum += i + sum_i 
            checked_numbers[i] = True 
            checked_numbers[sum_i] = True 
    return amicable_numbers_sum 

print(amicable_numbers_sum(999))  # Output: 504

Explanation:
Here we are using a function sum_proper_divisors(n) to find the sum of proper divisors of a number. We then iterate from 1 to the given limit, and for each number, we check if the sum of its proper divisors is a number that is not itself and has the same sum of proper divisors as the number. If so, we add both numbers to our sum and mark them as checked in the checked_numbers list.
"""

# Solution 2:
"""
