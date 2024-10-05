
def is_multiply_prime(a):
    if a < 100:
        return False
    for i in range(1, 30):
        if a % i == 0:
            if is_prime(i) and is_prime(a // i):
                return True
    return False

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

###

