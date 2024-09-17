def count_Primes_nums(n):
    primes = [2]
    for num in range(3, n, 2):
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
    return len(primes)

