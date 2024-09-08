def count_Primes_nums(n: int) -> int:
    if n <= 2:
        return 0
    primes = [2]
    for num in range(3, n, 2):
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
            if prime * prime > num:
                break
        if is_prime:
            primes.append(num)
    return len(primes)