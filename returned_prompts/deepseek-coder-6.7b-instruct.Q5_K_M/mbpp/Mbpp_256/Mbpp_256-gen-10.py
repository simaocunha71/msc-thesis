
def count_Primes_nums(n):
    sieve = [True] * n
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]: sieve[x*2::x] = [False] * len(sieve[x*2::x])
    return sum(sieve) - 2  # subtract 2 because 0 and 1 are not prime


