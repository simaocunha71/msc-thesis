def count_Primes_nums(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return 2 + count_Primes_nums(n - 1)