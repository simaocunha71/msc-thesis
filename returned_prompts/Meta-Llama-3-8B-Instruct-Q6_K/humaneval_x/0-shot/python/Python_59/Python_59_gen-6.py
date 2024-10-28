def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test cases
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))   # 2

# Explanation:
# The algorithm works by iterating from 2 to the square root of n, checking if n is divisible by the current number. If it is, we divide n by the current number and repeat the process. If n is not divisible by the current number, we increment the current number until it is. The process continues until n is reduced to its largest prime factor, which is the final value of n.

# The time complexity of this algorithm is O(sqrt(n)), as we only need to iterate up to the square root of n to find its largest prime factor. The space complexity is O(1), as we only use a constant amount of space to store the current number and the result.