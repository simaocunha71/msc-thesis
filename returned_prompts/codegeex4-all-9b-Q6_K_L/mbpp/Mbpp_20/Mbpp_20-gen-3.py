def is_woodall(n):
    if n < 2:
        return False

    sum = 0
    i = 1
    while n > 0:
        n, remainder = divmod(n, 2)
        if remainder == 1:
            sum += i
        i *= 2

    return sum == n

