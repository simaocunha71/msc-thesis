
def prime_fib(n: int):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        if is_prime(a):
            return a
    return a

def is_prime(n: int):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

