def armstrong_number(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(n))
        temp //= 10
    return n == sum