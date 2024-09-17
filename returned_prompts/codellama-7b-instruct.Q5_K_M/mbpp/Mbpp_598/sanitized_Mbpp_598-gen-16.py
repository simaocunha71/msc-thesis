def armstrong_number(n):
    sn = 0
    temp = n
    while temp > 0:
        sn += (temp % 10) ** 3
        temp //= 10
    return sn == n