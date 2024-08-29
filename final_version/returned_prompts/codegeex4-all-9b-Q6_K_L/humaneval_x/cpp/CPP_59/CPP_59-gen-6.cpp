def largest_prime_factor(n):
    '''Return the largest prime factor of n. Assume n > 1 and is not a prime.'''
    def is_prime(n):
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    largest_factor = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_factor = i
    return largest_factor

C:
def largest_prime_factor(n):
    '''Return the largest prime factor of n. Assume n > 1 and is not a prime.'''
    def is_prime(n):
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    largest_factor = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_factor = i
    return largest_factor

D:
def largest_prime_factor(n):
    '''Return the largest prime factor of n. Assume n > 1 and is not a prime.'''
    def is_prime(n):
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    largest_factor = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_factor = i
    return largest_factor

E:
def largest_prime_factor(n):
    '''Return the largest prime factor of n. Assume n > 1 and is not a prime.'''
    def is_prime(n):
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    largest_factor = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_factor = i
    return largest_factor

F:
def largest_prime_factor(n):
    '''Return the largest prime factor of n. Assume n > 1 and is not a prime.'''
    def is_prime(n):
        if n == 2:
            return True
