def newman_prime(n):
    if n == 1:
        return 2
    primes = [2]
    for i in range(3, 1000000, 2):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes[n-1]