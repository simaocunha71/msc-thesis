    def is_prime(n):
        """Check if a given number is a prime number"""
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    for i in primes:
        if i > a ** 0.5:
            break
        if a % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(is_multiply_prime(30))



# Created by Phantom10 on 08/09/2020

import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_multiply_prime(a):
    if a < 100:
        for i in range(2, a + 1):
            if is_prime(i) and is_prime(a // i):
                return True
    return False

print(is_multiply_prime(30))



# Created by Phantom10 on 08/09/2020

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
       