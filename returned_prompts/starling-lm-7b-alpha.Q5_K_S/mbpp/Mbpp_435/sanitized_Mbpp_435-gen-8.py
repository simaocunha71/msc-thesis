def last_Digit(num):
    if num < 0:
        return 0
    while num >= 10:
        num = num // 10
    return num % 10