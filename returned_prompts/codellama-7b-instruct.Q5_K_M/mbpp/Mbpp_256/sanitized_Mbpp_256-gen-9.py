def count_Primes_nums(n):
    if n <= 1:
        return 0
    is_prime = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return sum(is_prime)