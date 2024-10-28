def is_polite(n):
    count = 0
    num = 0
    while True:
        num += 1
        if is_prime(num):
            num += 1
        if is_prime(num):
            count += 1
        if count == n:
            return num - 1
        num += 1
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True