
def sum_common_divisors(a, b):
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            sum = i + sum_common_divisors(a//i, b//i)
    return sum


