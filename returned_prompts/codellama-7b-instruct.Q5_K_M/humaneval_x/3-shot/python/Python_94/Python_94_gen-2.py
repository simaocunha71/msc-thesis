    largest_prime = 0
    for i in lst:
        if is_prime(i) > largest_prime:
            largest_prime = is_prime(i)
    return sum(str(largest_prime))


def is_prime(n: int) -> int:
    if n == 1:
        return 1
    if n == 2 or n == 3:
        return n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n
