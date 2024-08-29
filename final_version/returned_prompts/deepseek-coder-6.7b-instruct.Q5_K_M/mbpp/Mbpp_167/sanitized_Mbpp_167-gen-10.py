def next_power_of_2(n):
    i = 0
    while True:
        if 2 ** i >= n:
            return 2 ** i
        i += 1