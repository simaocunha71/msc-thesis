
def highest_Power_of_2(n):
    power = 1
    while power <= n:
        power *= 2
    return power // 2


