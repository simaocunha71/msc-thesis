def highest_Power_of_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        while n != 0:
            n = n >> 1
        return n