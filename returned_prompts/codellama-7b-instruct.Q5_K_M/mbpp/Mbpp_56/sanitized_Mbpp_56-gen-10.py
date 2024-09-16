def check(num):
    if num == 10:
        return False
    else:
        return num == int(str(num)[::-1]) - 1