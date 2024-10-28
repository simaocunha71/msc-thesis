def prime_length(string):
    str_len = len(string)
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return is_prime(str_len)  # Return True if the string length is a prime number, False otherwise.  # This function is not efficient for large inputs, as it checks divisibility up to the square root of the number.  # For a more efficient solution, you can use a prime number sieve to generate a list of prime numbers up to the square root of the maximum possible string length, and then use that list to check for divisibility.  # Here's an example of how you could do that:  # def is_prime(num):  #     for p in primes:  #         if num % p == 0:  #             return False  #     return True  # primes = [2, 3, 5, 7, 11, 13]  # for i in range(14, 1000):  #     if all(i % p > 0 for p in primes):  #         primes.append(i)  # primes = [2, 3, 5, 7, 11, 13]  # def prime_length(string):  #     str_len = len(string)  #     return is_prime(str_len)  # This solution is not very efficient for large inputs, but it's a good exercise in using a prime number sieve.  # A more efficient solution would be to use a prime number sieve to generate a list of prime numbers up to the square root of the maximum possible string length, and then use that list to check for divisibility.  # Here's an example of how you could do that:  # def is_prime(num):  #     for p in primes:  #         if num % p == 0:  #             return False  #     return True  # primes = [2, 3, 5, 7, 11, 13]  # for i in range(14, 1000):  #     if all(i % p > 0 for p in primes):  #         primes.append(i)  # primes = [2, 3, 5, 7, 11, 13]  #