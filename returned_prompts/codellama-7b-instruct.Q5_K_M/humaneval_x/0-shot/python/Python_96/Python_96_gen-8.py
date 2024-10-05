
def count_up_to(n):
    if n <= 0:
        return []
    primes = [2]
    for i in range(3, n + 1, 2):
        if all(i % p != 0 for p in primes):
            primes.append(i)
    return primes

def count_up_to(n):
    return [i for i in range(2, n + 1) if all(i % num != 0 for num in range(2, int(i ** 0.5) + 1))]
