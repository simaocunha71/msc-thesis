def check(num):
    if str(num) == str(2 * (int(str(num)[::-1]) - 1)):
        return True
    else:
        return False