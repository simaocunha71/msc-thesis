def generate_prime(limit):
    primes = [2]
    num = 3
    while len(primes) < limit:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 2
    return primes
def newman_prime(n):
    primes = generate_prime(10000)
    return primes[n-1]