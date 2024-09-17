def validate(n):
    n = str(n)
    for digit in n:
        if int(digit) > 0 and n.count(digit) > int(digit):
            return False
    return True