def last_Digit(num):
    if num > 0:
        return num % 10
    elif num == 0:
        return 0
    else:
        return -(abs(num) % 10)