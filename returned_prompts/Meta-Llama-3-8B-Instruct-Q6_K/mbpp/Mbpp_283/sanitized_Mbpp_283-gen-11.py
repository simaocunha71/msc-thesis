def validate(n):
    str_n = str(n)
    for digit in str_n:
        if int(digit) > 0 and str_n.count(digit) > int(digit):
            return False
    return True