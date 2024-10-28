
def count_divisors(n):
    cnt = 0
    for i in range(1, (int)(n / 2) + 1):
        if (n % i == 0):
            cnt = cnt + 1
    return (cnt % 2 == 0)


