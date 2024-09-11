def count_Primes_nums(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(1 for i in range(2, n) if is_prime(i)) + 1