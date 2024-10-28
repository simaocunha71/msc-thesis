def newman_prime(n):
    if n == 1:
        return 2
    else:
        i = 1
        while True:
            i += 1
            if is_prime(i):
                n -= 1
                if n == 0:
                    return i
def is_prime(n):
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True