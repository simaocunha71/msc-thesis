def armstrong_number(n):
    temp = n
    total = 0
    while temp > 0:
        total += (temp % 10) ** 3
        temp //= 10
    return total == n



