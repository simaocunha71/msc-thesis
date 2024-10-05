from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(factorize(8))
print(factorize(25))
print(factorize(70))


def get_prime_factors(n: int) -> List[int]:
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(get_prime_factors(8))
print(get_prime_factors(25))
print(get_prime_factors(70))


# The code above works by repeatedly dividing the input number by the smallest possible factor. The result of each division becomes the new input number, and the process is repeated until the input number is 1. 
# This is the basic principle of prime factorization.

# The function factorize(n: int) returns the list of prime factors of the input number, in ascending order. 
# The function get_prime_factors(n: int) also returns the list of prime factors of the input number, but in ascending order.

# The two functions are almost identical, but factorize(n: int) returns the factors in the order they appear in the factorization process, while get_prime_factors(n: int) returns the factors in ascending order.

# The functions are designed to work with integers greater than 0. If a negative number or zero is passed as an argument, the functions will not return the correct result.

# In the provided examples, the function factorize(n: int) returns the list of prime factors of the input number, in the order they appear in the factorization process. For example, factorize(8) returns [2, 2, 2],