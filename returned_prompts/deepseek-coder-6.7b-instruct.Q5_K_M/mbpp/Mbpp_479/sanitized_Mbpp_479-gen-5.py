def first_Digit(n):
    while n > 0:
        digit = n % 10
        n = n // 10
        if n > 0:
            continue
        else:
            return digit