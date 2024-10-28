def highest_Power_of_2(n):
    if n == 0:
        return 0
    else:
        while (n & (n - 1)):
            n = n & (n - 1)
        return n