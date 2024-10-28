def is_undulating(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if int(str_num[i]) < int(str_num[i-1]):
            return False
    return True