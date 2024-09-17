def count_Primes_nums(n: int) -> int:
    if n < 2:
        return 0
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True