def is_undulating(num):
    temp = num
    while temp > 0:
        rem = temp % 10
        if rem != (temp // 10 % 10):
            return True
        temp = temp // 10
    return False