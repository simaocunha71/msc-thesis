

def skjkasdkd(lst):
    max_prime = 0
    for i in lst:
        if i > max_prime and is_prime(i):
            max_prime = i
    return sum(str(max_prime))


def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
