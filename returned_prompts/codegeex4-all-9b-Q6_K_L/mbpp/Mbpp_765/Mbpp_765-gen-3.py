def is_polite(n):
    if n == 1:
        return False
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
    return count == 1

def nth_polite(n):
    count = 0
    num = 1
    while count < n:
        if is_polite(num):
            count += 1
        num += 1
    return num

