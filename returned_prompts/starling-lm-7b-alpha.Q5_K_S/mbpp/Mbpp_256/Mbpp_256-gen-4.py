
def count_Primes_nums(num: int) -> int:
    count = 0
    for i in range(2, num + 1):
        if is_prime(i):
            count += 1
    return count

def is_prime(num: int) -> bool:
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = int(num ** 0.5) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            return False
    return True


