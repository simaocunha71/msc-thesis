
def count_Primes_nums(n):
    count = 0
    for i in range(2, n+1):
        if is_not_prime(i):
            continue
        count += 1
    return count


