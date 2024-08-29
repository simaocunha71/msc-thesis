def armstrong_number(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 0.3333333333333333 # 0.3333333333333333 is equivalent to 1/3 in python.
        temp //= 10

    return n == sum