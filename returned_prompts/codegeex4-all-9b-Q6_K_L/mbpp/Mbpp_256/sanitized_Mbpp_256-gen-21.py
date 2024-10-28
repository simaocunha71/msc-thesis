def count_Primes_nums(n: int) -> int:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    return sum(is_prime(i) for i in range(n))