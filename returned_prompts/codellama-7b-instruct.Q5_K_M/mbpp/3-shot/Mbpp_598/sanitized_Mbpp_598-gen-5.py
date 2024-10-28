def armstrong_number(n):
    sum = 0
    temp = n
    while temp > 0:
        sum += (temp % 10) ** 3
        temp //= 10
    return sum == n