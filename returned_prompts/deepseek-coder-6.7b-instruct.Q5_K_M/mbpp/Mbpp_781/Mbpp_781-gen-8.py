"""
The function will take an integer as an input and return True if the count of divisors is even, else it will return False.

Here is a python function to solve this problem.
"""

def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count % 2 == 0

print(count_divisors(10)) # should return True
"""
This function works by iterating from 1 to n (inclusive) and checking whether n is divisible by the current number. If it is, the count is incremented. The function then returns whether the count of divisors is even.
"""

# Test case 2
