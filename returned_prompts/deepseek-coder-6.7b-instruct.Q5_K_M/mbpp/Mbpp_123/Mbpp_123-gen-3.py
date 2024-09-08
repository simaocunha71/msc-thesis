"""
First, we need to understand what an amicable number is. Two numbers are amicable if the sum of the proper divisors of each number equals the other number.

For example, 220 and 284 are amicable because the sum of the proper divisors of 220 (1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110) is 284, and the sum of the proper divisors of 284 (1 + 2 + 4 + 71 + 142) is 220.

We will use the following steps to solve this problem:
1. Create a function that returns a list of proper divisors of a number.
2. Create a function that returns the sum of the proper divisors of a number.
3. Loop through all numbers from 1 to the specified number, and for each number, check if it is an amicable number. If it is, add it to the sum.
4. Return the sum.
"""

def proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)
            else:
                divisors.extend([i, n // i])
    return divisors

def d(n):
    return sum(proper_divisors(n))

def amicable_numbers_sum(n):
    result = 0
    for i in range(1, n+1):
        if i == d(d(i)) and i != d(i):
            result += i
    return result

print(amicable_numbers_sum(999)) # 504
"""

