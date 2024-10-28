
def count_up_to(n):
    if n < 0:
        return []
    primes = []
    for i in range(2, n+1):
        if i < n and i % 2 == 0:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes



