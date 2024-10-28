
def highest_Power_of_2(n):
    if n == 0:
        return 0
    i = 1
    while 2 ** i <= n:
        i *= 2
    return 2 ** (i // 2)


