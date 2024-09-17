
def highest_Power_of_2(n):
    i = 1
    while i <= n:
        i = i << 1
    return i >> 1


