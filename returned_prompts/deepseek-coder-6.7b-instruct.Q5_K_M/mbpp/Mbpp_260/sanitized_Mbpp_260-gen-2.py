def newman_prime(n):
    newman_primes = [2, 3, 5, 7, 11]
    if n <= 5:
        return newman_primes[n-1]
    else:
        next_prime = newman_primes[-1] + 1
        while True:
            if is_newman_prime(next_prime):
                newman_primes.append(next_prime)
                if len(newman_primes) == n:
                    return newman_primes[-1]
            next_prime += 1
def is_newman_prime(num):
    if num in [2, 3, 5, 7, 11]:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True