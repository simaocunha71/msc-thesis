def is_polite(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if int(str_num[i]) == i + 1:
            continue
        elif int(str_num[i]) == i + 2:
            continue
        else:
            return False
    return True