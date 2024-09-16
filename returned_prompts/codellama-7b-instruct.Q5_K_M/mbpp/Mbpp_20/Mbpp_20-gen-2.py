def is_woodall(num):
    str_num = str(num)
    for i in range(len(str_num) - 1):
        if int(str_num[i]) != int(str_num[i+1]):
            return False
    return True
