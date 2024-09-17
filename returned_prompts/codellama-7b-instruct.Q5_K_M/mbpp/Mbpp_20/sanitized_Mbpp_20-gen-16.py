def is_woodall(num: int) -> bool:
    str_num = str(num)
    if len(str_num) != 3:
        return False
    if str_num[0] != str_num[1] or str_num[1] != str_num[2]:
        return False
    return True