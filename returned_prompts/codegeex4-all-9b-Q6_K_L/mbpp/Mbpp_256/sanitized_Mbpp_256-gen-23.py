def count_Primes_nums(n):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    return sum(is_prime(i) for i in range(2, n))