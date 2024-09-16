
def nth_polite(n):
    if n == 1:
        return 1
    i = 1
    while True:
        i += 1
        if is_polite(i):
            n -= 1
            if n == 0:
                return i

def is_polite(n):
    count = 0
    while n > 0:
        count += 1
        if n % 10 == 0:
            n //= 10
        else:
            n = n // 100 + n % 10
    return count == 4

nth_polite(1)
# 1
nth_polite(2)
# 11
