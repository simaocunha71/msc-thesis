"""
We will solve the problem using a simple loop that checks each number from 1 to the given integer. If the number is a divisor (i.e., if the integer divided by the number has no remainder), we will increment the count.
"""

def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

print(divisor(15))  # 4
assert divisor(15) == 4
"""
This function will return the correct number of divisors for any given integer.
"""

"""

"""

# Exercise 2:

