def count_Primes_nums(num):
    if num < 2:
        return 0
    count = 0
    for i in range(2, num):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count