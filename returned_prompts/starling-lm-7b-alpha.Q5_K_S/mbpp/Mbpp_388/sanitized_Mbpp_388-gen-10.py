def highest_Power_of_2(n):
    p = 1
    while (p * 2 <= n):
        p *= 2
    return p