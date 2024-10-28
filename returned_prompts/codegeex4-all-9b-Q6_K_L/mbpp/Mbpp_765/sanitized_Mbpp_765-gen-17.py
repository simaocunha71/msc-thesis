def is_polite(n):
    num = 1
    count = 0
    while count < n:
        num += 1
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
    return num