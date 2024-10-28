def validate(num: int) -> bool:
    num = str(num)
    for digit in num:
        if int(digit) > num.count(digit):
            return False
    return True