def count_Primes_nums(n: int) -> int:
    prime_count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            prime_count += 1
    return prime_count
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True