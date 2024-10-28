def is_woodall(num):
    if num < 100:
        return False
    str_num = str(num)
    if str_num[0] == str_num[1] == str_num[2] == str_num[3] == str_num[4]:
        return True
    else:
        return False

