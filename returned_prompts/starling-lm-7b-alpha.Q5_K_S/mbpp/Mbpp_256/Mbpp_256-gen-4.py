"""
def count_Primes_nums(x):
    primes = [2, 3, 5]
    while x > 7:
        x += 1
        is_prime = True
        for p in primes:
            if x % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return len(primes)
"""

