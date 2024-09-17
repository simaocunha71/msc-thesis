def count_Primes_nums(n):
    count = 0
    for i in range(2, n + 1):
        if all(i % j != 0 for j in range(2, i)):
            count += 1
    return count