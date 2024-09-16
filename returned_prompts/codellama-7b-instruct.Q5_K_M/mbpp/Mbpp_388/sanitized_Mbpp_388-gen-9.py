def highest_Power_of_2(n):
    if n == 1:
        return 1
    else:
        i = 1
        while 2 ** i <= n:
            i += 1
        return 2 ** (i - 1)