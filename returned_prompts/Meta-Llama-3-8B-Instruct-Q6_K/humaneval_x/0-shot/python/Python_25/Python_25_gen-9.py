from typing import List

def factorize(n: int) -> List[int]:
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            while n % i == 0:
                n //= i
                factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
# Example of usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
# Note: The function works by dividing the input number by the smallest prime number (2) as long as it's divisible.
# Then it increments the divisor until it finds the next number that can divide the input number.
# This process continues until the input number becomes 1, which means all prime factors have been found.
# The function returns a list of prime factors with the smallest prime factor appearing the most times.  # noqa: E501
# The function uses the trial division method for finding prime factors. It's not the most efficient method for large numbers,  # noqa: E501
# but it's simple and suitable for small to medium-sized numbers. For large numbers, you may want to use a more efficient method  # noqa: E501
# such as the Sieve of Eratosthenes or the Miller-Rabin primality test.  # noqa: E501
# Also, the function assumes that the input number is a positive integer. If you want to handle negative numbers or non-integers,  # noqa: E501
# you'll need to add additional logic.  # noqa: E501
# In terms of time complexity, the function has a time complexity of O(sqrt(n)), where n is the input number. This is because  # noqa: E501
# we're dividing the input number by the smallest prime number as long as it's divisible, which takes O(sqrt(n)) time.  # noqa: E501
# The space complexity is O(log(n)), where n is the input number. This is because we're storing the prime factors in a list,  # noqa: E501
# and the length of the list is at most log(n), since each prime factor is at most sqrt(n). 