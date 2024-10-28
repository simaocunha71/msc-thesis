def is_polite(n):
    total = 0
    num = 1
    while True:
        total += num
        if total >= n:
            return total - n + 1
        num += 1