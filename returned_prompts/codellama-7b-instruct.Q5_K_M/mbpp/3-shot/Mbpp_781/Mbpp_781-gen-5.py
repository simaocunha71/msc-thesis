
def count_divisors(n):
    divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors += 1
    if divisors % 2 == 0:
        return True
    else:
        return False


