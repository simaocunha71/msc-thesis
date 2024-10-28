

def skjkasdkd(lst):
    largest = 0
    for i in lst:
        if i > largest and is_prime(i):
            largest = i
    return sum(str(largest))


def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
