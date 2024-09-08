def count_Primes_nums(n):
    if n <= 2:
        return 0
    primes = [2]
    for num in range(3, n, 2):
        for p in primes:
            if num % p == 0:
                break
            if p * p > num:
                primes.append(num)
                break
    return len(primes)