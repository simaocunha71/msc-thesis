
def count_divisors(n):
    if n == 1:
        return False
    num_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            num_divisors += 1
    return num_divisors % 2 == 0


