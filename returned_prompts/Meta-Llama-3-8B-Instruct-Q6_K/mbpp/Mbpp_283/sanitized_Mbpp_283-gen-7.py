def validate(n):
    n_str = str(n)
    for digit in n_str:
        if int(digit) > 0 and n_str.count(digit) > int(digit):
            return False
    return True