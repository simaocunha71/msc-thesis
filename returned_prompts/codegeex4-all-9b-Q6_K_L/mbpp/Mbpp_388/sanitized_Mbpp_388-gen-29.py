def highest_Power_of_2(n):
    res = 0
    i = 1
    while i <= n:
        res = i
        i = i * 2
    return res