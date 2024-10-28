    def largest_prime_factor(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
        return n
# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2


Python code to find the largest prime factor of a given number.

This function works by dividing the input number `n` by the smallest prime number, which is 2, as long as it is divisible. Then it increments the divisor until it finds the next number that can divide `n`, which will be a prime number. This process is repeated until `n` is reduced to 1. The last non-1 value of `n` will be the largest prime factor.

The function uses a while loop to continuously divide `n` by the smallest prime number (2) until `n` is no longer divisible. If `n` is divisible, it is divided and the loop continues. If `n` is not divisible, the divisor is incremented and the loop continues. This process is repeated until `n` is reduced to 1. The last non-1 value of `n` will be the largest prime factor.

The function is then tested with the values 13195 and 2048, and the results are printed to the console. The output is 29 for 13195 and 2 for 2048, which are the correct largest prime factors for these numbers.