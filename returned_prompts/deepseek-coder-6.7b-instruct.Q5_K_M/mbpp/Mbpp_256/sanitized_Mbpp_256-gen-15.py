def count_Primes_nums(n):
    count = 0
    for num in range(2, n):
        if is_not_prime(num):
            count += 1
    return count