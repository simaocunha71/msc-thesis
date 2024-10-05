

def skjkasdkd(lst):
    primes = []
    for i in lst:
        if is_prime(i):
            primes.append(i)
    return sum(list(map(int, str(max(primes)))))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# 

