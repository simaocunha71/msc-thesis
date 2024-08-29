"""
def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count % 2 == 0

print(count_ivisors(10))
"""

E:
"""
The function count_divisors takes an integer n as an argument and returns True if the count of its divisors is even, and False otherwise.
"""

# Answer
def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count % 2 == 0

print(count_divisors(10))  # Output: True

# Explanation: The divisors of 10 are 1, 2, 5, 10. So, the count of divisors is 4 which is even. Therefore, the function returns True.
<jupyter_output>
True
<jupyter_text>
