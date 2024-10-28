    # Code to find the largest prime factor of a given number
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
    # Python code for the problem
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

# In this code, we first initialize a variable i to 2. Then we enter a loop that continues until i * i is less than or equal to n. If n is not divisible by i, we increment i by 1. If n is divisible by i, we divide n by i and continue the loop. This process continues until n is no longer divisible by any number, at which point we return n as the largest prime factor. For example, for the input 13195, the code will divide 13195 by 2, then 5, then 29, and finally return 29 as the largest prime factor.
# When we run this code with the inputs 13195 and 2048, we get the expected outputs 29 and 2, respectively. The code works correctly for all inputs greater than 1 and not prime.