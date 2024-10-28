# A helper function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# A helper function to find the largest prime factor
def largest_prime_factor(n):
    for i in range(n, 1, -1):
        if n % i == 0 and is_prime(i):
            return i

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2

B:
# A helper function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# A helper function to find the largest prime factor
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n if is_prime(n) else largest_prime_factor(n)

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2

C:
# A helper function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# A helper function to find the largest prime factor
def largest_prime_factor(n):
    prime_factors = []
    for i in range(2, n+1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    return max([p for p in prime_factors if is_prime(p)])

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2

D:
# A helper function to check if a number is prime
def is_prime(num):
    if num < 