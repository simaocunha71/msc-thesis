def all_Characters_Same(str):
    if len(str) == 0:
        return True
    first = str[0]
    for i in range(len(str)):
        if first != str[i]:
            return False
    return True


