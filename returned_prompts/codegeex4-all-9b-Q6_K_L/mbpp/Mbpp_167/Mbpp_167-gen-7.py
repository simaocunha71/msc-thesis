def next_power_of_2(n):
    if n > 0:
        return 2 ** int(math.ceil(math.log(n, 2)))
    else:
        return 1