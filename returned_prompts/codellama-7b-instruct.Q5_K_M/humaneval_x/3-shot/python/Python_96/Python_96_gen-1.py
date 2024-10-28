    if n == 0:
        return []
    if n == 1:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]
    prime_numbers = []
    for i in range(2, n):
        if is_prime(i):
            prime_numbers.append(i)
        if len(prime_numbers) == n - 1:
            return prime_numbers
    return prime_numbers


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
    return True


