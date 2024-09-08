def first_Digit(num):
    while num > 0:
        digit = num % 10
        if num == num:
            return digit
        num = num // 10
    return -1