
def count_divisors(n):
    cnt = 0
    for i in range(1, (int(n**0.5) + 1)):
        if n % i == 0:
            if n / i == i:
                cnt = cnt + 1
            else:
                cnt = cnt + 2
    return cnt % 2 == 0


