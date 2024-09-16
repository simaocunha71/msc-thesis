def newman_prime(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        num = 2**n - 1
        while not is_prime(num):
            num += 2
        return num


def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
