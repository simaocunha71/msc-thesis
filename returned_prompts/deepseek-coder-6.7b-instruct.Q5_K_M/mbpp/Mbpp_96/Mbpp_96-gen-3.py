def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

print(divisor(15))

#output: 4

"""
Explanation:
The function divisor takes an integer n as an input.
It then iterates from 1 to n (both inclusive).
For each number, it checks if n is divisible by the current number (i.e., n is evenly divisible).
If n is divisible, it increases the count by 1.
Finally, it returns the count.
The number of divisors of a number n is equal to the count of numbers from 1 to n that n is divisible by.
Therefore, the function works correctly.
"""

# Alternate solution
def divisor(n):
    count = 0
    i = 1
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

print(divisor(15))

#output: 4

# Alternate solution
def divisor(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
    return count

print(divisor(15))

#output: 4

"""
Explanation:
The function divisor takes an integer n as an input.
It then iterates from 1 to sqrt(n) (both inclusive).
For each number, it checks if n is divisible by the current number.
If n is divisible, it increases the count by 1.
If the number and its corresponding quotient are the same (e.g., 1 and 15 in 15), it increases the count by 1.
If not, it increases the count by 2 (for both the number and its corresponding quotient).
Finally, it returns the count.
The number of divisors of a number n is equal to the count of numbers from 1 to sqrt(n) that n