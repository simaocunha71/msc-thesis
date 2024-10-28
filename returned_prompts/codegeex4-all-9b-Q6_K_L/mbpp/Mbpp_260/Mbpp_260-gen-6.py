import math
def newman_prime(n: int) -> int:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def newman_shanks_williams_prime(n: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        while len(primes) < n:
            next_prime = primes[-1] + 1
            while not is_prime(next_prime):
                next_prime += 1
            primes.append(next_prime)
        return primes[n-1]

    return newman_shanks_williams_prime(n)