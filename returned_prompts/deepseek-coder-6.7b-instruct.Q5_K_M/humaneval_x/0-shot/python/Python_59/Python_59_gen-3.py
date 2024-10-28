
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)


"""
Explanation:

The function works by dividing the input number n by the smallest prime number, 2, as long as the result is not 1. If the result is not divisible by 2, the function increments the divisor by 1. This process continues until the input number is reduced to 1, at which point the function returns the final divisor as the largest prime factor.

For example, consider the number 13195. The function first divides by 2, reducing the number to 6597. It then increments the divisor to 3 and continues, reducing the number to 2265. The divisor is incremented to 5 and the number is reduced to 453. The divisor is incremented to 7 and the number is reduced to 61. The divisor is incremented to 11 and the number is reduced to 5. The divisor is incremented to 13 and the number is now 1. The function returns 1 as the largest prime factor.
"""

#15_prime_sieve_eratosthenes.py
# Prime Sieve - Eratosthenes

