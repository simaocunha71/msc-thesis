def validate(n):
    num = str(n)
    for digit in set(num):
        if num.count(digit) > int(digit):
            return False
    return True