def next_power_of_2(n):
    if n < 0:
        return -next_power_of_2(-n)
    if n <= 0:
        return 1
    i = 2
    while i <= n:
        i *= 2
    return i