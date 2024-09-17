
def count_Primes_nums(n):
    if n < 2:
        return 0
    count = 1
    i = 2
    while i < n:
        if is_prime(i):
            count += 1
        i += 1
    return count

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_div = int(num**0.5) + 1
    for i in range(3, max_div, 2):
        if num % i == 0:
            return False
    return True


