def validate(num):
    num = str(num)
    for i in num:
        if num.count(i) > int(i):
            return False
    return True