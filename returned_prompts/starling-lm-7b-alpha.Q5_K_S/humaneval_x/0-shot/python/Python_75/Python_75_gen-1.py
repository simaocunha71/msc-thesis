    def is_prime(n):
        """Check if a number is prime"""
        if n==1:
            return False
        for i in range(2, int(n**0.5 + 1)):
            if n%i==0:
                return False
        return True

    def find_prime(n):
        """Find first n prime numbers"""
        primes = []
        for i in range(2, n+1):
            if is_prime(i):
                primes.append(i)
        return primes

    def is_multiply_prime(a):
        """Check if a number is multiplication of 3 prime numbers"""
        if a<=1:
            return False
        if is_prime(a):
            return True
        primes = find_prime(int(a**0.5))
        for i in range(len(primes)):
            for j in range(i+1,len(primes)):
                if primes[i]*primes[j]>a:
                    break
                if a%(primes[i]*primes[j])==0:
                    return True
        return False

    return is_multiply_prime(a)



def find_prime(n):
    """Find first n prime numbers"""
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(n):
    """Check if a number is prime"""
    if n==1:
        return False
    for i in range(2, int(n**0.5 + 1)):
        if n%i==0:
            return False
    return True


# is_multiply_prime(30) == True
# 30 = 2 * 3 * 5

# is_multiply_prime(32) == False
# 32 = 2 * 2 * 2 * 2 * 2

# is_multiply_prime(31) == False
# 31 is a prime number

#