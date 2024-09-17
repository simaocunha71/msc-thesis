def validate(n):
    str_n = str(n)
    for digit in set(str_n):
        if str_n.count(digit) > int(digit):
            return False
    return True