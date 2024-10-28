
def count_up_to(n):
    primes = []
    if n > 0:
        for i in range(2, n):
            if is_prime(i):
                primes.append(i)
        primes.append(n)
    return primes

def is_prime(n):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False
