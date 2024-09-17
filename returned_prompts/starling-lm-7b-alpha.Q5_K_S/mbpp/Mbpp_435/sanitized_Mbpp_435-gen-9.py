def last_Digit(n):
    if n < 10:
        return n
    else:
        return last_Digit(n % 10)