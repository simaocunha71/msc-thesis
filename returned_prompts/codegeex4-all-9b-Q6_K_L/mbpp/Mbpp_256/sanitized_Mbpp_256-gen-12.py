def count_Primes_nums(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = 0
    for i in range(2, n):
        if is_prime(i):
            prime_count += 1
    return prime_count