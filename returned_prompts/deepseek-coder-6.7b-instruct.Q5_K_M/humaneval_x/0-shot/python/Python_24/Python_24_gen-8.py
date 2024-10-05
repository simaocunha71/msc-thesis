
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

print(largest_divisor(15))

# Answer: 5

# Explanation: The function starts from n-1 and goes down to 1. The first number that n is divisible by is the largest divisor, so the function returns that number. For example, 15 is divisible by 5 (15/5 = 3). 

# Note: This solution is not the most efficient for large numbers because it checks every number. A more efficient solution would use a prime factorization approach or use a sieve to find the largest prime factor.
<jupyter_output>
5
<jupyter_text>
