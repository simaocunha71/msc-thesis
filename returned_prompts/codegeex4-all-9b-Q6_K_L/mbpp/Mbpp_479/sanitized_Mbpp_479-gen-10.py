def first_Digit(num):
    if num < 0:
        num = -num
    while num >= 10:
        num = num // 10
    return num