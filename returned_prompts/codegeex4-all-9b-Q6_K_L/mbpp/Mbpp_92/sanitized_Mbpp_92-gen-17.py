def is_undulating(n):
    str_num = str(n)
    for i in range(len(str_num) - 1):
        if str_num[i] == str_num[i+1]:
            return False
    return True