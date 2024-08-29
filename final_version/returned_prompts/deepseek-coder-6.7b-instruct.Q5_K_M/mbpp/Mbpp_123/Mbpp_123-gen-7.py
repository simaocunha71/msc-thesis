"""
First, we need to understand what an amicable number is. 
An amicable number is a number where the sum of its proper divisors is equal to another number where the sum of its proper divisors is equal to the first number.

For example, the smallest pair of amicable numbers is (220, 284). 
The proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; these numbers sum to 284. 
Similarly, the proper divisors of 284 are 1, 2, 4, 71 and 142; these numbers sum to 220.

We will write a function that will first calculate the sum of proper divisors for each number from 1 to the specified number, and then check if the sum of proper divisors is equal to another number and if they are not the same number.

Here is the Python code:
"""

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

print(amicable_numbers_sum(999))  # Output: 504

This code first calculates the sum of proper divisors for each number up to the specified limit