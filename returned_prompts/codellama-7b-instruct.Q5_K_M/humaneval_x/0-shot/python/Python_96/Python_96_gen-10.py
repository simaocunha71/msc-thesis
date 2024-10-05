
def count_up_to(n):
    primes = []
    if n == 0:
        return primes
    for i in range(2, n+1):
        if i > 1:
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    return primes

