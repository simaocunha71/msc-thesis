def armstrong_number(num):
    n = num
    sum = 0
    while n != 0:
        r = n % 10
        sum += r ** 3
        n //= 10
    if sum == num:
        return True
    else:
        return False