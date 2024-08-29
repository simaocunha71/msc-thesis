def validate(num):
    num = str(num)
    for digit in num:
        if num.count(digit) > int(digit):
            return False
    return True

print(validate(1234)) # True


