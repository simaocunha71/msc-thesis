
    if not lst or len(lst) == 0:
        return 0

    # find the largest prime number
    largest_prime = 0
    for num in lst:
        if is_prime(num) and num > largest_prime:
            largest_prime = num

    return sum(str(largest_prime))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
