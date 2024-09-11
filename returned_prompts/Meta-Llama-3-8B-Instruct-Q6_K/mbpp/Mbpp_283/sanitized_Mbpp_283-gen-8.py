def validate(n):
    for digit in str(n):
        if int(digit) > 0 and str(n).count(digit) > int(digit):
            return False
    return True