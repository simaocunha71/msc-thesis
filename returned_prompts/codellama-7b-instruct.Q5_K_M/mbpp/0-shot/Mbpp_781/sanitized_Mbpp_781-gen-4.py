def count_divisors(n):
    return len(list(filter(lambda x: n % x == 0, range(1, int(n ** 0.5) + 1))))