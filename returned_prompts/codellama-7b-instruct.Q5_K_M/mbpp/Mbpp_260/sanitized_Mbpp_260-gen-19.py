def newman_prime(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    i = 1
    while True:
        if is_prime(newman_prime(i)):
            i += 1
        else:
            return newman_prime(i)
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True